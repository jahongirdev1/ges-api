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
                    'image': 'https://instagram.fakx4-2.fna.fbcdn.net/v/t51.29350-15/390942906_876748464034650_8908176971284239684_n.webp?stp=dst-jpg_e35_p1080x1080_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fakx4-2.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2AHiqrsAbNyrENIDpwEhtGFMHXHKZe5WcBfwT0Zn_2u4Q_2SAnOjJXjOrxF3sxl4N08&_nc_ohc=K9qErlPFZEUQ7kNvgHEOC0w&_nc_gid=487f0d671463469c9120821ecca04c42&edm=APoiHPcBAAAA&ccb=7-5&ig_cache_key=MzIxMzU2MDE2NTg4OTU2NjYzOQ%3D%3D.3-ccb7-5&oh=00_AYBvf7DarR0YbO_u1jmxxrwKB5pApC4vDaeVrRH5EX_bmQ&oe=67B51F5B&_nc_sid=22de04',
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
                    'image': 'https://instagram.fakx4-2.fna.fbcdn.net/v/t51.29350-15/390942906_876748464034650_8908176971284239684_n.webp?stp=dst-jpg_e35_p1080x1080_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fakx4-2.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2AHiqrsAbNyrENIDpwEhtGFMHXHKZe5WcBfwT0Zn_2u4Q_2SAnOjJXjOrxF3sxl4N08&_nc_ohc=K9qErlPFZEUQ7kNvgHEOC0w&_nc_gid=487f0d671463469c9120821ecca04c42&edm=APoiHPcBAAAA&ccb=7-5&ig_cache_key=MzIxMzU2MDE2NTg4OTU2NjYzOQ%3D%3D.3-ccb7-5&oh=00_AYBvf7DarR0YbO_u1jmxxrwKB5pApC4vDaeVrRH5EX_bmQ&oe=67B51F5B&_nc_sid=22de04',
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
                    'image': 'https://instagram.fakx4-2.fna.fbcdn.net/v/t51.29350-15/390942906_876748464034650_8908176971284239684_n.webp?stp=dst-jpg_e35_p1080x1080_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fakx4-2.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2AHiqrsAbNyrENIDpwEhtGFMHXHKZe5WcBfwT0Zn_2u4Q_2SAnOjJXjOrxF3sxl4N08&_nc_ohc=K9qErlPFZEUQ7kNvgHEOC0w&_nc_gid=487f0d671463469c9120821ecca04c42&edm=APoiHPcBAAAA&ccb=7-5&ig_cache_key=MzIxMzU2MDE2NTg4OTU2NjYzOQ%3D%3D.3-ccb7-5&oh=00_AYBvf7DarR0YbO_u1jmxxrwKB5pApC4vDaeVrRH5EX_bmQ&oe=67B51F5B&_nc_sid=22de04',
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

        if not insert or not insert.inserted_ids:
            return self.error('Failed to create the course.')

        return self.success({'inserted_id': str(insert.inserted_ids)})


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
