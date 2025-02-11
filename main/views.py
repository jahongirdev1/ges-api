from bson import ObjectId
from core.db import db
from core.handler import BaseHandler

class StoryHandler(BaseHandler):
    async def get(self):
        stories = await db.stories.find({'status': 0}).to_list(None)

        grouped_stories = {}
        for story in stories:
            owner_id = str(story.get('owner_id', story['_id']))
            if owner_id not in grouped_stories:
                grouped_stories[owner_id] = {
                    'id': owner_id,
                    'image': story.get('profile_image', 'https://example.com/default-avatar.jpg'),
                    'stories': []
                }
            grouped_stories[owner_id]['stories'].append({
                'id': str(story['_id']),
                'link': story['link'],
                'type': story['type'],
                'description': story.get('description', '')
            })

        return self.success({'items': list(grouped_stories.values())})

    async def post(self):
        body = self.body()
        link = body.get('link')
        story_type = body.get('type')
        description = body.get('description')
        owner_id = body.get('owner_id')


        if not link or not story_type:
            return self.error('Both "link" and "type" are required.')

        if story_type not in ['image', 'video']:
            return self.error('Invalid story type. Use "image" or "video".')

        # Owner ma'lumotlarini olish
        owner = await db.owners.find_one({'_id': ObjectId(owner_id)})
        profile_image = owner.get('profile_image') if owner else 'https://example.com/default-avatar.jpg'

        insert = await db.stories.insert_one({
            'link': link,
            'type': story_type,
            'description': description,
            'owner_id': owner_id,
            'profile_image': profile_image,
            'status': 0
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

        delete_result = await db.stories.delete_one({'_id': ObjectId(story_id)})

        if delete_result.deleted_count == 0:
            return self.error('Delete failed')

        return self.success({'deleted_id': story_id})


class StoryItemHandler(BaseHandler):
    async def get(self, story_id):
        if not ObjectId.is_valid(story_id):
            return self.error('Invalid story id')

        story = await db.stories.find_one({'_id': ObjectId(story_id)})
        if not story:
            return self.error('Story not found')

        return self.success({
            'id': str(story['_id']),
            'link': story['link'],
            'type': story['type'],
            'description': story.get('description', '')
        })

    async def post(self, story_id):
        if not ObjectId.is_valid(story_id):
            return self.error('Invalid story id')

        body = self.body()
        link = body.get('link')
        story_type = body.get('type')
        description = body.get('description')

        if story_type not in ['image', 'video']:
            return self.error('Invalid story type. Use "image" or "video".')

        update_result = await db.stories.update_one(
            {'_id': ObjectId(story_id)},
            {'$set': {
                'link': link,
                'type': story_type,
                'description': description,
                'status': 0
            }}
        )

        if update_result.modified_count == 0:
            return self.error('Update failed')

        return self.success({'updated_id': story_id})

    async def delete(self, story_id):
        if not ObjectId.is_valid(story_id):
            return self.error('Invalid story id')

        delete_result = await db.stories.delete_one({'_id': ObjectId(story_id)})

        if delete_result.deleted_count == 0:
            return self.error('Delete failed')

        return self.success({'deleted_id': story_id})
