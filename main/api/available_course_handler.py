from core.handler import BaseHandler
from bson import ObjectId
from core.db import db


class AvailableCourseHandler(BaseHandler):
    async def get(self):
        courses = await db.courses.find({'status': 0}).to_list(None)

        for course in courses:
            course['_id'] = str(course['_id'])

        return self.success({'items': courses})

    async def post(self):
        insert = await db.courses.insert_many(
            [
                {
                    'image': 'data:image/jpeg;base64,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',
                    'display_name': 'Dilorom Mirsaliyeva',
                    'course_title': 'IELTS',
                    'venue': 'Sayram',
                    'date_week': 'Пн, Ср, Пт',
                    'time': '10:00 - 12:00',
                    'place_count': 15,
                    'students': 8,
                    'description': '',
                    'status': 0,
                },
                {
                    'image': 'data:image/jpeg;base64,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',
                    'display_name': 'Dilorom Mirsaliyeva',
                    'course_title': 'IELTS',
                    'venue': 'Shymkent',
                    'date_week': 'Пн, Ср, Пт',
                    'time': '10:00 - 12:00',
                    'place_count': 15,
                    'students': 3,
                    'description': 'description',
                    'status': 0,
                },
                {
                    'image': 'data:image/jpeg;base64,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',
                    'display_name': 'Dilorom Mirsaliyeva',
                    'course_title': 'IELTS',
                    'venue': 'Sayram',
                    'date_week': 'Пн, Ср, Пт',
                    'time': '10:00 - 12:00',
                    'place_count': 15,
                    'students': 5,
                    'description': 'description',
                    'status': 0,
                },
            ])

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the course.')

        return self.success({'inserted_id': str(insert.inserted_id)})


class AvailableCourseItemHandler(BaseHandler):
    async def put(self, course_id):
        if not ObjectId.is_valid(course_id):
            return self.error('Invalid course ID.')

        body = self.body()
        update_data = {}

        teacher_image = body.get('teacher_image')
        teacher_display_name = body.get('teacher_display_name')
        course_title = body.get('course_title')
        price = body.get('price')
        status = body.get('status', 0)
        description = body.get('description')

        update_data['status'] = status

        if teacher_image:
            if not isinstance(teacher_image, str) or not teacher_image.strip():
                return self.error('The "teacher_image" field must be a non-empty string.')
            update_data['teacher_image'] = teacher_image.strip()

        if teacher_display_name:
            if not isinstance(teacher_display_name, str) or not teacher_display_name.strip():
                return self.error('The "teacher_display_name" field must be a non-empty string.')
            update_data['teacher_display_name'] = teacher_display_name.strip()

        if course_title:
            if not isinstance(course_title, str) or not course_title.strip():
                return self.error('The "course_title" field must be a non-empty string.')
            update_data['course_title'] = course_title.strip()

        if price is not None:
            if not isinstance(price, int) or price <= 0:
                return self.error('The "price" field must be a positive integer.')
            update_data['price'] = price

        if description is not None:
            if not isinstance(description, str):
                return self.error('The "description" field must be a string.')
            update_data['description'] = description.strip()

        if not update_data:
            return self.error('No valid fields provided for update.')

        update_result = await db.courses.update_one(
            {'_id': ObjectId(course_id)},
            {'$set': update_data}
        )

        if update_result.modified_count == 0:
            return self.error('Course update failed or no changes were made.')

        return self.success({'updated_id': course_id, 'updated_fields': list(update_data.keys())})

    async def delete(self, course_id):
        if not ObjectId.is_valid(course_id):
            return self.error('Invalid course ID.')

        delete_result = await db.courses.update_one(
            {'_id': ObjectId(course_id)},
            {'$set': {'status': -1}}
        )

        if delete_result.modified_count == 0:
            return self.error('Course deletion failed or course already deleted.')

        return self.success({'deleted_id': course_id, 'status': -1})
