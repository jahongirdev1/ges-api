from core.handler import BaseHandler
from datetime import datetime
from bson import ObjectId
from core.db import db


class EventHandler(BaseHandler):
    async def get(self):
        events = await db.events.find({'status': 0}).to_list(None)

        for event in events:
            event['_id'] = str(event['_id'])

        return self.success({'items': events})

    async def post(self):
        body = self.body()
        image = body.get('image')
        title = body.get('title')
        branch = body.get('branch')
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        description = body.get('description', '')

        insert = await db.events.insert_one({
            'image': image,
            'title': title,
            'branch': branch,
            'date': date,
            'description': description,
            'status': 0,
        })

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the event.')

        return self.success({'inserted_id': str(insert.inserted_id)})


class EventsItemHandler(BaseHandler):
    async def put(self, event_id):
        if not ObjectId.is_valid(event_id):
            return self.error('Invalid event ID.')

        body = self.body()
        update_data = {}

        image = body.get('image')
        title = body.get('title')
        branch = body.get('branch')
        status = body.get('status')
        description = body.get('description')

        if status is not None:
            if not isinstance(status, int):
                return self.error('The "status" field must be an integer.')
            update_data['status'] = status

        if image:
            if not isinstance(image, str) or not image.strip():
                return self.error('The "image" field must be a non-empty string.')
            update_data['image'] = image.strip()

        if title:
            if not isinstance(title, str) or not title.strip():
                return self.error('The "title" field must be a non-empty string.')
            update_data['title'] = title.strip()

        if branch:
            if not isinstance(branch, str) or not branch.strip():
                return self.error('The "branch" field must be a non-empty string.')
            update_data['branch'] = branch.strip()

        if description is not None:
            if not isinstance(description, str):
                return self.error('The "description" field must be a string.')
            update_data['description'] = description.strip()

        if not update_data:
            return self.error('No valid fields provided for update.')

        update_result = await db.events.update_one(
            {'_id': ObjectId(event_id)},
            {'$set': update_data}
        )

        if update_result.modified_count == 0:
            return self.error('Event update failed or no changes were made.')

        return self.success({'updated_id': event_id, 'updated_fields': list(update_data.keys())})

    async def delete(self, event_id):
        if not ObjectId.is_valid(event_id):
            return self.error('Invalid event ID.')

        delete_result = await db.events.update_one(
            {'_id': ObjectId(event_id)},
            {'$set': {'status': -1}}
        )

        if delete_result.modified_count == 0:
            return self.error('Event deletion failed or event already deleted.')

        return self.success({'deleted_id': event_id, 'status': -1})
