from main.api.story_handler import StoryHandler, StoryItemHandler
from main.api.product_handler import  ProductHandler, ProductItemHandler
from main.api.achievement_handler import AchievementHandler, AchievementsItemHandler


URLS = [
    (r"/api/mobile/stories", StoryHandler),
    (r"/api/mobile/stories/([a-f0-9]{24})", StoryItemHandler),

    (r"/api/mobile/products", ProductHandler),
    (r"/api/mobile/products/([a-f0-9]{24})", ProductItemHandler),

    (r"/api/mobile/achievements", AchievementHandler),
    (r"/api/mobile/achievements/([a-f0-9]{24})", AchievementsItemHandler),

]