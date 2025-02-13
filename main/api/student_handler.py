from core.handler import BaseHandler
from bson import ObjectId
from core.db import db


class StudentHandler(BaseHandler):
    async def get(self):
        students = await db.students.find({'status': 0}).to_list(None)

        for student in students:
            student['_id'] = str(student['_id'])

        return self.success({'items': students})

    async def post(self):
        insert = await db.students.insert_one({
            "last_name": "Rahmanshikov",
            "first_name": "Jahongir",
            "middle_name": "",
            "avatar": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkS8v2vSpIzK2HCPWDdfZP3vbvQhEm5fxuwkNENSNSswbBoWScLb0h3GjVFqgZB9FEpSg&usqp=CAU",
            "group_added_time": "2024-02-12T10:00:00Z",
            "invite_discount": 10,
            "bonus_discount": 5,
            "school": "Example High School",
            "klass": "10A",
            "new_group_id": "12345",
            "shift": "morning",
            "group_type": "regular",
            "date": "2024-02-12",
            "sex": "male",
            "level_id": "1",
            "filial_id": "2",
            "subject_id": "3",
            "address": "123 Example Street",
            "subject": "English",
            "phone": "+77020718600",
            "dop_phone": "+0987654321",
            "phone_father": "+1122334455",
            "phone_mather": "+2233445566",
            "email": "jahonggir617@gmail.com",
            "iin": "999999999999",
            "copies": 2,
            "student_id_for_combination": "98765",
            "coins": 125,
            "balance": 11450,
            "next_payment": "02 Feb, 2025",
            "next_payment_amount": 30000,
            'status': 0,
        })

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the student.')

        return self.success({'inserted_id': str(insert.inserted_id)})


class CoinHistoryHandler(BaseHandler):
    async def get(self):
        coin_histories = await db.coin_history.find({}).to_list(None)

        for coin_history in coin_histories:
            coin_history['_id'] = str(coin_history['_id'])

        return self.success({'items': coin_histores})

    async def post(self):
        insert = await db.coin_history.insert_many([
            {'date': '2025-02-13', 'count': 10},
            {'date': '2025-02-14', 'count': 15},
            {'date': '2025-02-15', 'count': 20},
            {'date': '2025-02-16', 'count': 25},
            {'date': '2025-02-17', 'count': 30},
            {'date': '2025-02-18', 'count': 35},
            {'date': '2025-02-19', 'count': 40},
            {'date': '2025-02-20', 'count': 45},
            {'date': '2025-02-21', 'count': 50},
            {'date': '2025-02-22', 'count': 55},
        ])

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the coin.')

        return self.success({'inserted_id': str(insert.inserted_id)})


class PaymentHistoryHandler(BaseHandler):
    async def get(self):
        payment_histories = await db.payment_history.find({}).to_list(None)

        for payment_history in payment_histories:
            payment_history['_id'] = str(payment_history['_id'])

        return self.success({'items': payment_histores})

    async def post(self):
        insert = await db.payment_history.insert_many([
            {
                "title": "Intermediate",
                "date": "2025-02-07",
                "amount": 14000,
                "isOnline": true
            },
            {
                "title": "Intermediate",
                "date": "2025-01-07",
                "amount": 14000,
                "isOnline": false
            },
            {
                "title": "Intermediate",
                "date": "2024-12-07",
                "amount": 14000,
                "isOnline": true
            },
            {
                "title": "Intermediate",
                "date": "2024-11-07",
                "amount": 14000,
                "isOnline": true
            },
            {
                "title": "Pre Intermediate",
                "date": "2025-02-07",
                "amount": 14000,
                "isOnline": false
            },
            {
                "title": "Intermediate",
                "date": "2025-02-07",
                "amount": 14000,
                "isOnline": true
            },
            {
                "title": "Intermediate",
                "date": "2025-02-07",
                "amount": 14000,
                "isOnline": true
            },
            {
                "title": "Intermediate",
                "date": "2025-02-07",
                "amount": 14000,
                "isOnline": true
            }
        ])

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the payment.')

        return self.success({'inserted_id': str(insert.inserted_id)})


class CertificateHandler(BaseHandler):
    async def get(self):
        certificates = await db.certificates.find({}).to_list(None)

        for certificate in certificates:
            certificate['_id'] = str(certificate['_id'])

        return self.success({'items': certificates})

    async def post(self):
        insert = await db.certificates.insert_many([
            {
                "image": "https://cdn.vectorstock.com/i/1000v/16/73/certificate-template-vector-23631673.jpg",
                "title": "Intermediate",
                "link": "https://mohirdevbucket.s3.eu-central-1.amazonaws.com/certificates/cert-7f01ce2f-8912-4bd1-9683-1b5457269c23-prac--0uSpkcs7.pdf"
            },
            {
                "image": "https://cdn.vectorstock.com/i/1000v/16/73/certificate-template-vector-23631673.jpg",
                "title": "Pre Intermediate",
                "link": "https://mohirdevbucket.s3.eu-central-1.amazonaws.com/certificates/cert-7f01ce2f-8912-4bd1-9683-1b5457269c23-prac--0uSpkcs7.pdf"
            },
            {
                "image": "https://cdn.vectorstock.com/i/1000v/16/73/certificate-template-vector-23631673.jpg",
                "title": "Elementary",
                "link": "https://mohirdevbucket.s3.eu-central-1.amazonaws.com/certificates/cert-7f01ce2f-8912-4bd1-9683-1b5457269c23-prac--0uSpkcs7.pdf"
            },
            {
                "image": "https://cdn.vectorstock.com/i/1000v/16/73/certificate-template-vector-23631673.jpg",
                "title": "Beginner",
                "link": "https://mohirdevbucket.s3.eu-central-1.amazonaws.com/certificates/cert-7f01ce2f-8912-4bd1-9683-1b5457269c23-prac--0uSpkcs7.pdf"
            },
            {
                "image": "https://cdn.vectorstock.com/i/1000v/16/73/certificate-template-vector-23631673.jpg",
                "title": "Primary 4",
                "link": "https://mohirdevbucket.s3.eu-central-1.amazonaws.com/certificates/cert-7f01ce2f-8912-4bd1-9683-1b5457269c23-prac--0uSpkcs7.pdf"
            },
            {
                "image": "https://cdn.vectorstock.com/i/1000v/16/73/certificate-template-vector-23631673.jpg",
                "title": "Primary 3",
                "link": "https://mohirdevbucket.s3.eu-central-1.amazonaws.com/certificates/cert-7f01ce2f-8912-4bd1-9683-1b5457269c23-prac--0uSpkcs7.pdf"
            }
        ])

        if not insert or not insert.inserted_id:
            return self.error('Failed to create the certificates.')

        return self.success({'inserted_id': str(insert.inserted_id)})
