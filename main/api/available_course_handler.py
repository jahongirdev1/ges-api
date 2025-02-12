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
        body = self.body()
        teacher_image = body.get('teacher_image')
        teacher_display_name = body.get('teacher_display_name')
        course_title = body.get('course_title')
        price = body.get('price')
        description = body.get('description', '')

        if not teacher_image or not isinstance(teacher_image, str) or not teacher_image.strip():
            return self.error('The "teacher_image" field is required and must be a non-empty string.')

        if not teacher_display_name or not isinstance(teacher_display_name, str) or not teacher_display_name.strip():
            return self.error('The "teacher_display_name" field is required and must be a non-empty string.')

        if not course_title or not isinstance(course_title, str) or not course_title.strip():
            return self.error('The "course_title" field is required and must be a non-empty string.')

        if not isinstance(price, int) or price <= 0:
            return self.error('The "price" field is required and must be a positive integer.')

        insert = await db.courses.insert_one({
            'teacher_image': teacher_image.strip(),
            'teacher_display_name': teacher_display_name.strip(),
            'course_title': course_title,
            'price': price,
            'description': description,
            'status': 0,
        })

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
