import twitter
from twitter_key import keys
import datetime as dt
api = twitter.Api(**keys)
now = dt.datetime.now()
day_str = now.strftime("%A, %B %d")
hour_str = now.strftime("%H:%M")
api.PostUpdate(f'[WakeUp 🤖]\nHello,\ntoday is {day_str}, and it\'s {hour_str} in Paris.\nHave a nice day!')