from core.handler import BaseHandler
from bson import ObjectId
from core.db import db


class AchievementHandler(BaseHandler):
    async def get(self):
        achievements = await db.achievements.find({'status': 0}).to_list(None)

        for achievement in achievements:
            achievement['_id'] = str(achievement['_id'])

        return self.success({'items': achievements})

    async def post(self):
        body = self.body()
        title = body.get('title')

        if not title or not title.strip():
            return self.error('The "title" field is required.')

        insert = await db.achievement_category.insert_one({
            'title': title.strip(),
            'status': 0,
        })

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the achievement category.')

        return self.success({'inserted_id': str(insert.inserted_id)})


class AchievementsItemHandler(BaseHandler):
    async def get(self, parent_id):
        if not ObjectId.is_valid(parent_id):
            return self.error('Invalid parent_id')

        achievements = await db.achievements.find({'parent_id': ObjectId(parent_id), 'status': 0}).to_list(None)

        for achievement in achievements:
            achievement['_id'] = str(achievement['_id'])
            achievement['parent_id'] = str(achievement['parent_id'])

        return self.success({'items': achievements})

    async def post(self, parent_id):
        body = self.body()

        image = body.get('image')
        display_name = body.get('display_name')
        description = body.get('description')

        if not image or not image.strip():
            return self.error('The "image" field is required.')
        if not display_name or not display_name.strip():
            return self.error('The "display_name" field is required.')
        if not description or not description.strip():
            return self.error('The "description" field is required.')

        if not ObjectId.is_valid(parent_id):
            return self.error('Invalid parent_id')

        insert = await db.achievements.insert_one({
            'image': image.strip(),
            'display_name': display_name.strip(),
            'description': description.strip(),
            'parent_id': ObjectId(parent_id),
            'status': 0,
        })

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the achievement.')

        return self.success({'inserted_id': str(insert.inserted_id)})
