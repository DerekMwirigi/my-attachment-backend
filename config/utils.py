       
from datetime import datetime, timedelta

from dateutil import tz

def date_filter_split(datefilter):
    if datefilter:
        if datefilter != "None":
            date_array = datefilter.split('--')
            start_date = date_array[0].strip()
            end_date = date_array[1].strip()
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            start_date_with_tz = datetime(start_date_obj.year, start_date_obj.month, start_date_obj.day,
                                          tzinfo=tz.gettz('Africa/Nairobi')).astimezone(tz.gettz('UTC'))
            end_date_with_tz = datetime(end_date_obj.year, end_date_obj.month, end_date_obj.day,
                                        tzinfo=tz.gettz('Africa/Nairobi')).astimezone(tz.gettz('UTC')) + timedelta(
                days=1)
        else:
            today = datetime.utcnow().date()
            start_date_with_tz = datetime(today.year, today.month, today.day,
                                          tzinfo=tz.gettz('Africa/Nairobi')).astimezone(tz.gettz('UTC'))
            end_date_with_tz = datetime(today.year, today.month, today.day,
                                        tzinfo=tz.gettz('Africa/Nairobi')).astimezone(
                tz.gettz('UTC')) + timedelta(days=1)
    else:
        today = datetime.utcnow().date()
        start_date_with_tz = datetime(today.year, today.month, today.day, tzinfo=tz.gettz('Africa/Nairobi')).astimezone(
            tz.gettz('UTC'))
        end_date_with_tz = datetime(today.year, today.month, today.day, tzinfo=tz.gettz('Africa/Nairobi')).astimezone(
            tz.gettz('UTC')) + timedelta(days=1)

    return start_date_with_tz, end_date_with_tz
