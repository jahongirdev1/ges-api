from main.views import MainHandler, MainItemHandler

URLS = [
    ('/users', MainHandler),
    ('/users/([^/]+)', MainItemHandler),
]
