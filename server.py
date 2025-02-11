import asyncio

import tornado

from core.db import db
from main.urls import URLS
from settings import settings


async def before_server_start():
    loop = asyncio.get_event_loop()
    db.initialize(loop)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.current().run_sync(before_server_start)
    app = tornado.web.Application(URLS)
    app.listen(settings['port'])
    tornado.ioloop.IOLoop.current().start()
