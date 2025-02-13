from core.handler import BaseHandler
from datetime import datetime
from bson import ObjectId
from core.db import db


class NotificationHandler(BaseHandler):

    async def get(self):
        notifications = await db.notifications.find({}).to_list(None)

        for notification in notifications:
            notification['_id'] = str(notification['_id'])

        return self.success({'items': notifications})

    async def post(self):
        insert = await db.notifications.insert_many([
            {
                'title': 'Home Work',
                'description': 'Vocabulary, ex 1,2,3,4',
                'date': '2025-02-13 12:30',
                'screen_name': 'home_work'
            },
            {
                'title': 'GES EVENT',
                'description': 'Events GES.....',
                'date': '2025-02-13 12:30',
                'screen_name': 'events'
            },
            {
                'title': 'Home Work',
                'description': 'Vocabulary, ex 1,2,3,4',
                'date': '2025-02-13 12:30',
                'screen_name': 'home_work'
            },
            {
                'title': 'Home Work',
                'description': 'Vocabulary, ex 1,2,3,4',
                'date': '2025-02-13 12:30',
                'screen_name': 'home_work'
            },
            {
                'title': 'GES EVENT',
                'description': 'Events GES.....',
                'date': '2025-02-13 12:30',
                'screen_name': 'events'
            },
        ])


        if not insert or not insert.inserted_ids:
            return self.error('Failed to create the notification.')

        return self.success({'inserted_ids': [str(id) for id in insert.inserted_ids]})
