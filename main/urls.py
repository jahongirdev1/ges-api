from main.views import StoryHandler, StoryItemHandler

URLS = [
    (r"/api/mobile/stories", StoryHandler),
    (r"/api/mobile/stories/([a-f0-9]{24})", StoryItemHandler),
]