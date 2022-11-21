import datetime
from common.config import settings

def now_time():
    return datetime.datetime.now(settings.TIMEZONE)
