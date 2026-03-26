from datetime import datetime
import pytz
a=pytz.timezone("Asia/Tokyo")
b=datetime.now(a)
print(b)
