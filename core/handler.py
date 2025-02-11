import tornado
from tornado.escape import json_decode

from core.objects import encoder


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    def params(self):
        return {key: self.get_query_argument(key) for key in self.request.arguments}

    def body(self):
        return json_decode(self.request.body or '{}')

    def success(self, data: dict):
        data['_success'] = True
        chunk = encoder.encode(data)
        return super().write(chunk)

    def error(self, message: str):
        return self.write({
            '_success': False,
            'message': message
        })
