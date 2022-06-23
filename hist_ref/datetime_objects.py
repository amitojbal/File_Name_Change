from datetime import datetime as dt
import dateutil.parser

   

    # DateTime objects
    # print(f_util_date)
    # print("f_current_dt", f_util_date)
    # print("f_date", f_util_date.date())
    # print("f_year", f_util_date.year)
    # print("f_month", f_util_date.month)
    # print("f_day", f_util_date.day)
    # print("f_time", f_util_date.time())
    # print("f_hour", f_util_date.hour)
    # print("f_minute", f_util_date.minute)
    # print("f_sec", f_util_date.second)
    # print("f_mic secs", f_util_date.microsecond)

    
    
    #provide month number
    month_num = str(f_util_date.month)
        
    datetime_object = dt.strptime(month_num, "%m")

    f_month_name = datetime_object.strftime("%B")