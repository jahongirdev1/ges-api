from core.handler import BaseHandler
from bson import ObjectId
from core.db import db


class ProductHandler(BaseHandler):
    async def get(self):
        products = await db.products.find({'status': 0}).to_list(None)

        for product in products:
            product['_id'] = str(product['_id'])

        return self.success({'items': products})

    async def post(self):
        body = self.body()
        image = body.get('image')
        title = body.get('title')
        price = body.get('price')
        description = body.get('description', '')

        # Validation
        if not image or not isinstance(image, str) or not image.strip():
            return self.error('The "image" field is required and must be a non-empty string.')

        if not title or not isinstance(title, str) or not title.strip():
            return self.error('The "title" field is required and must be a non-empty string.')

        if price is None or not isinstance(price, (int, float)) or price < 0:
            return self.error('The "price" field is required and must be a positive number.')

        insert = await db.products.insert_one({
            'image': image.strip(),
            'title': title.strip(),
            'price': price,
            'description': description.strip(),
            'status': 0,
        })

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the product.')

        return self.success({'inserted_id': str(insert.inserted_id)})


class ProductItemHandler(BaseHandler):
    async def put(self, product_id):
        if not ObjectId.is_valid(product_id):
            return self.error('Invalid product ID.')

        body = self.body()
        update_fields = {k: v for k, v in body.items() if k != 'id' and v != ''}

        if not update_fields:
            return self.error('No valid fields provided to update.')

        update_result = await db.products.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': update_fields}
        )

        if update_result.modified_count == 0:
            return self.error('Update failed or no changes detected.')

        return self.success({'updated_id': product_id})

    async def delete(self, product_id):
        if not ObjectId.is_valid(product_id):
            return self.error('Invalid product ID.')

        delete_result = await db.products.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': {'status': -1}}
        )

        if delete_result.modified_count == 0:
            return self.error('Product deletion failed or product already deleted.')

        return self.success({'deleted_id': product_id, 'status': -1})
