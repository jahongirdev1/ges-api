from main.api.story_handler import StoryHandler, StoryItemHandler
from main.api.product_handler import  ProductHandler, ProductItemHandler
URLS = [
    (r"/api/mobile/stories", StoryHandler),
    (r"/api/mobile/stories/([a-f0-9]{24})", StoryItemHandler),

    (r"/api/mobile/products", ProductHandler),
    (r"/api/mobile/products/([a-f0-9]{24})", ProductItemHandler),

]