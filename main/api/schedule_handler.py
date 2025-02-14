from core.handler import BaseHandler
from bson import ObjectId
from core.db import db


class ScheduleHandler(BaseHandler):
    async def get(self):
        courses = await db.schedule.find({}).to_list(None)

        for course in courses:
            course['_id'] = str(course['_id'])

        return self.success({'items': courses})


    async def post(self):
        insert = await db.schedule.insert_many([
            {
                'image': 'https://instagram.fakx4-2.fna.fbcdn.net/v/t51.29350-15/390942906_876748464034650_8908176971284239684_n.webp?stp=dst-jpg_e35_p1080x1080_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fakx4-2.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2AHiqrsAbNyrENIDpwEhtGFMHXHKZe5WcBfwT0Zn_2u4Q_2SAnOjJXjOrxF3sxl4N08&_nc_ohc=K9qErlPFZEUQ7kNvgHEOC0w&_nc_gid=487f0d671463469c9120821ecca04c42&edm=APoiHPcBAAAA&ccb=7-5&ig_cache_key=MzIxMzU2MDE2NTg4OTU2NjYzOQ%3D%3D.3-ccb7-5&oh=00_AYBvf7DarR0YbO_u1jmxxrwKB5pApC4vDaeVrRH5EX_bmQ&oe=67B51F5B&_nc_sid=22de04',
                'display_name': 'Dilorom Mirsaliyeva',
                'course_title': 'IELTS',
                'venue': 'Sayram',
                'date_week': 'Пн, Ср, Пт',
                'time': '10:00 - 12:00',
                'room':'208',
                'description': '',
                'status': 0,
            },
            {
                'image': 'https://instagram.fakx4-2.fna.fbcdn.net/v/t51.29350-15/390942906_876748464034650_8908176971284239684_n.webp?stp=dst-jpg_e35_p1080x1080_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fakx4-2.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2AHiqrsAbNyrENIDpwEhtGFMHXHKZe5WcBfwT0Zn_2u4Q_2SAnOjJXjOrxF3sxl4N08&_nc_ohc=K9qErlPFZEUQ7kNvgHEOC0w&_nc_gid=487f0d671463469c9120821ecca04c42&edm=APoiHPcBAAAA&ccb=7-5&ig_cache_key=MzIxMzU2MDE2NTg4OTU2NjYzOQ%3D%3D.3-ccb7-5&oh=00_AYBvf7DarR0YbO_u1jmxxrwKB5pApC4vDaeVrRH5EX_bmQ&oe=67B51F5B&_nc_sid=22de04',
                'display_name': 'Dilorom Mirsaliyeva',
                'course_title': 'Beginner',
                'venue': 'Sayram',
                'date_week': 'Пн, Ср, Пт',
                'time': '10:00 - 12:00',
                'room': '210',
                'description': '',
                'status': 0,
            },
            {
                'image': 'https://instagram.fakx4-2.fna.fbcdn.net/v/t51.29350-15/390942906_876748464034650_8908176971284239684_n.webp?stp=dst-jpg_e35_p1080x1080_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fakx4-2.fna.fbcdn.net&_nc_cat=106&_nc_oc=Q6cZ2AHiqrsAbNyrENIDpwEhtGFMHXHKZe5WcBfwT0Zn_2u4Q_2SAnOjJXjOrxF3sxl4N08&_nc_ohc=K9qErlPFZEUQ7kNvgHEOC0w&_nc_gid=487f0d671463469c9120821ecca04c42&edm=APoiHPcBAAAA&ccb=7-5&ig_cache_key=MzIxMzU2MDE2NTg4OTU2NjYzOQ%3D%3D.3-ccb7-5&oh=00_AYBvf7DarR0YbO_u1jmxxrwKB5pApC4vDaeVrRH5EX_bmQ&oe=67B51F5B&_nc_sid=22de04',
                'display_name': 'Dilorom Mirsaliyeva',
                'course_title': 'Elementary',
                'venue': 'Sayram',
                'date_week': 'Пн, Ср, Пт',
                'time': '09:00 - 11:00',
                'room': '200',
                'description': '',
                'status': 0,
            },
        ])

        if not insert or not insert.inserted_ids:
            return self.error('Failed to create the event.')

        return self.success({'inserted_ids': [str(id) for id in insert.inserted_ids]})