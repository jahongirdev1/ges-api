from bson import ObjectId
from core.db import db
from core.handler import BaseHandler

class StoryHandler(BaseHandler):
    async def get(self):
        stories = await db.stories.find({'status': 0}).to_list(None)

        for parent in stories:
            parent['_id'] = str(parent['_id'])
            if 'stories' in parent:
                for story in parent['stories']:
                    if '_id' in story:
                        story['_id'] = str(story['_id'])

        return self.success({'items': stories})
    async def post(self):
        body = self.body()
        image = body.get('image')

        if not image:
            return  self.error('image required')

        insert = await  db.stories.insert_one({
            'image': image,
            'stories': [],
            'status': 0,
        })

        if not insert or not insert.inserted_id:
            return self.error('Operation failed')

        return self.success({'inserted_id': str(insert.inserted_id)})
    async def put(self):
        body = self.body()
        story_id = body.get('id')

        if not ObjectId.is_valid(story_id):
            return self.error('Invalid story id')

        update_result = await db.stories.update_one(
            {'_id': ObjectId(story_id)},
            {'$set': body}
        )

        if update_result.modified_count == 0:
            return self.error('Update failed')

        return self.success({'updated_id': story_id})
    async def delete(self):
        body = self.body()
        story_id = body.get('id')

        if not ObjectId.is_valid(story_id):
            return self.error('Invalid story id')

        delete_result = await db.stories.update_one(
            {'_id': ObjectId(story_id)},
            {'$set': {'status': -1}}
        )

        if delete_result.modified_count == 0:
            return self.error('Delete (status update) failed')

        return self.success({'deleted_id': story_id, 'status': -1})

class StoryItemHandler(BaseHandler):
    async def get(self, story_id):
        if not ObjectId.is_valid(story_id):
            return self.error('Invalid story id')

        story = await db.stories.find_one({'_id': ObjectId(story_id)})
        if not story:
            return self.error('Story not found')

        story['_id'] = str(story['_id'])

        return self.success({
            'id': story['_id'],
            'image': story.get('image'),
            'status': story.get('status', 0),
            'description': story.get('description', ''),
            'stories': story.get('stories', [])
        })
    async def post(self, parent_id):
        if not ObjectId.is_valid(parent_id):
            return self.error('Invalid story id')

        body = self.body()
        link = body.get('link')
        story_type = body.get('type')
        duration = body.get('duration', 0)
        description = body.get('description')

        if story_type not in ['image', 'video']:
            return self.error('Invalid story type. Use "image" or "video".')

        parent_story = await db.stories.find_one({'_id': ObjectId(parent_id)})

        if not parent_story:
            return self.error('Parent story not found.')

        new_story = {
            'link': link,
            'type': story_type,
            'duration': duration,
            'description': description,
            'parent_id': parent_id,
            'status': 0
        }

        update_result = await db.stories.update_one(
            {'_id': ObjectId(parent_id)},
            {'$push': {'stories': new_story}}
        )

        if update_result.modified_count == 0:
            return self.error('Failed to add story.')

        return self.success({'message':'Story added successfully'}),
    async def put(self, story_id):
        if not ObjectId.is_valid(story_id):
            return self.error('Invalid story id')

        body = self.body()
        update_fields = {k: v for k, v in body.items() if k != 'id'}

        if not update_fields:
            return self.error('No fields provided to update.')

        update_result = await db.stories.update_one(
            {'_id': ObjectId(story_id)},
            {'$set': update_fields}
        )

        if update_result.modified_count == 0:
            return self.error('Update failed or no changes detected.')

        return self.success({'updated_id': story_id})
    async def delete(self, story_id):
        if not ObjectId.is_valid(story_id):
            return self.error('Invalid story id')

        delete_result = await db.stories.update_one(
            {'_id': ObjectId(story_id)},
            {'$set': {'status': -1}}
        )

        if delete_result.modified_count == 0:
            return self.error('Delete (status update) failed')

        return self.success({'deleted_id': story_id, 'status': -1})
