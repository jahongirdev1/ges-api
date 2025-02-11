from bson import ObjectId

from core.db import db
from core.handler import BaseHandler


class MainHandler(BaseHandler):
    async def get(self):
        params = self.params()


        filters = {}
        if params.get('event'):
            filters['event'] = params['event']

        if params.get('count'):
            filters['count'] = params['count']

        items = await db.extra.find(filters).to_list(None)
        return self.success({'items': items})

    async def post(self):
        body = self.body()
        event = body.get('event')
        count = body.get('count')
        insert = await db.extra.insert_one({
            'event': event,
            'count': count,
            'status': 0
        })
        if not insert or not insert.inserted_id:
            return self.error('Operation failed')

        return self.success({'inserted_id': insert.inserted_id})


class MainItemHandler(BaseHandler):
    async def get(self, item_id):
        if not ObjectId.is_valid(item_id):
            return self.error('Invalid item id')

        item = await db.extra.find_one({'_id': ObjectId(item_id)})
        return self.success({'item': item})

    async def post(self, item_id):
        if not ObjectId.is_valid(item_id):
            return self.error('Invalid item id')

        body = self.body()

        event = body.get('event')
        count = body.get('count')

        await db.extra.update_one({'_id': ObjectId(item_id)}, {'$set': {
            'event': event,
            'count': count,
            'status': 0
        }})
        return self.success({})
