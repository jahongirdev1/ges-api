from main.api.story_handler import StoryHandler, StoryItemHandler

URLS = [
    (r"/api/mobile/stories", StoryHandler),
    (r"/api/", StoryHandler),
    (r"/api/mobile/stories/([a-f0-9]{24})", StoryItemHandler),
]