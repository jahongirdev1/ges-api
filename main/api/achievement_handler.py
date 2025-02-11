from core.handler import BaseHandler
from bson import ObjectId
from core.db import db


class AchievementHandler(BaseHandler):
    async def post(self):
        body = self.body()
        achievement_type = body.get('type')
        image = body.get('image')
        display_name = body.get('display_name')
        description = body.get('description')

        # Validation
        if not achievement_type:
            return self.error('The "type" field is required.')
        if not image:
            return self.error('The "image" field is required.')
        if not display_name:
            return self.error('The "display_name" field is required.')
        if not description:
            return self.error('The "description" field is required.')

        insert = await db.achievement.insert_one({
            'type': achievement_type,
            'image': image,
            'display_name': display_name,
            'description': description,
            'status': 0,
        })

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the achievement.')

        return self.success({'inserted_id': str(insert.inserted_id)})


class AchievementsItemHandler(BaseHandler):
    async def get(self, achievement_type):
        if not achievement_type:
            return self.error('The "type" field is required.')

        achievements = await db.achievement.find({'status': 0, 'type': achievement_type}).to_list(None)

        for achievement in achievements:
            achievement['_id'] = str(achievement['_id'])

        return self.success({'items': achievements})

    async def put(self, achievement_id):
        if not achievement_id or not ObjectId.is_valid(achievement_id):
            return self.error('Invalid achievement ID.')

        update_fields = {k: v for k, v in body.items() if k != 'id' and v is not None}

        if not update_fields:
            return self.error('No fields provided to update.')

        update_result = await db.achievement.update_one(
            {'_id': ObjectId(achievement_id)},
            {'$set': update_fields}
        )

        if update_result.modified_count == 0:
            return self.error('Update failed or no changes detected.')

        return self.success({'updated_id': achievement_id})

    async def delete(self, achievement_id):
        if not achievement_id or not ObjectId.is_valid(achievement_id):
            return self.error('Invalid achievement ID.')

        delete_result = await db.achievement.update_one(
            {'_id': ObjectId(achievement_id)},
            {'$set': {'status': -1}}
        )

        if delete_result.modified_count == 0:
            return self.error('Delete operation failed or achievement already deleted.')

        return self.success({'deleted_id': achievement_id, 'status': -1})
