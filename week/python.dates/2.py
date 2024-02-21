import datetime
from datetime import date
x=date.today()

print("keshe:",x-datetime.timedelta(days=1))
print("bugyn:",x)
print("erten:",x+datetime.timedelta(days=1))