from main.api.story_handler import StoryHandler, StoryItemHandler
from main.api.product_handler import  ProductHandler, ProductItemHandler
from main.api.achievement_handler import AchievementHandler, AchievementsItemHandler
from  main.api.available_course_handler import AvailableCourseHandler, AvailableCourseItemHandler
from main.api.events_handler import EventHandler, EventsItemHandler
from main.api.student_handler import StudentHandler, CoinHistoryHandler, PaymentHistoryHandler, CertificateHandler
from main.api.notification_handler import NotificationHandler
from main.api.schedule_handler import ScheduleHandler

URLS = [
    (r"/api/mobile/stories", StoryHandler),
    (r"/api/mobile/stories/([a-f0-9]{24})", StoryItemHandler),

    (r"/api/mobile/products", ProductHandler),
    (r"/api/mobile/products/([a-f0-9]{24})", ProductItemHandler),

    (r"/api/mobile/achievements", AchievementHandler),
    (r"/api/mobile/achievements/([a-f0-9]{24})", AchievementsItemHandler),

    (r"/api/mobile/courses", AvailableCourseHandler),
    (r"/api/mobile/courses/([a-f0-9]{24})", AvailableCourseItemHandler),

    (r"/api/mobile/events", EventHandler),
    (r"/api/mobile/events/([a-f0-9]{24})", EventsItemHandler),

    (r"/api/mobile/students", StudentHandler),

    (r"/api/mobile/coin-history", CoinHistoryHandler),

    (r"/api/mobile/payment-history", PaymentHistoryHandler),

    (r"/api/mobile/certificates", CertificateHandler),

    (r"/api/mobile/notifications", NotificationHandler),

    (r"/api/mobile/schedules", ScheduleHandler),

]