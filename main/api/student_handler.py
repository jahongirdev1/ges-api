from core.handler import BaseHandler
from bson import ObjectId
from core.db import db


class StudentHandler(BaseHandler):
    async def get(self):
        products = await db.students.find({'status': 0}).to_list(None)

        for product in products:
            product['_id'] = str(product['_id'])

        return self.success({'items': products})

    async def post(self):
        body = self.body()
        last_name = body.get('last_name')
        first_name = body.get('first_name')
        middle_name = body.get('middle_name')
        avatar = body.get('avatar')
        group_added_time = body.get('group_added_time')
        invite_discount = body.get('invite_discount')
        bonus_discount = body.get('bonus_discount')
        school = body.get('school')
        klass = body.get('klass')
        new_group_id = body.get('new_group_id')
        shift = body.get('shift')
        group_type = body.get('group_type')
        date = body.get('date')
        sex = body.get('sex')
        level_id = body.get('level_id')
        filial_id = body.get('filial_id')
        subject_id = body.get('subject_id')
        address = body.get('address')
        subject = body.get('subject')
        phone = body.get('phone')
        dop_phone = body.get('dop_phone')
        phone_father = body.get('phone_father')
        phone_mather = body.get('phone_mather')
        email = body.get('email')
        iin = body.get('iin')
        copies = body.get('copies')
        student_id_for_combination = body.get('student_id_for_combination')
        coin = body.get('coin')
        balance = body.get('balance')

        insert = await db.students.insert_one({
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'avatar': avatar,
            'group_added_time': group_added_time,
            'invite_discount': invite_discount,
            'bonus_discount': bonus_discount,
            'school': school,
            'klass': klass,
            'new_group_id': new_group_id,
            'shift': shift,
            'group_type': group_type,
            'date': date,
            'sex': sex,
            'level_id': level_id,
            'filial_id': filial_id,
            'subject_id': subject_id,
            'address': address,
            'subject': subject,
            'phone': phone,
            'dop_phone': dop_phone,
            'phone_father': phone_father,
            'phone_mather': phone_mather,
            'email': email,
            'iin': iin,
            'copies': copies,
            'student_id_for_combination': student_id_for_combination,
            'coin': coin,
            'balance': balance,
            'status': 0,
        })

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the student.')

        return self.success({'inserted_id': str(insert.inserted_id)})

    async def delete(self):
        body = self.body()
        student_id = body.get('_id')

        if not student_id:
            return self.error("Student ID is required.")

        result = await db.students.delete_one({'_id': ObjectId(student_id)})

        if result.deleted_count == 0:
            return self.error("Failed to delete student or student not found.")

        return self.success({'deleted_id': student_id})
