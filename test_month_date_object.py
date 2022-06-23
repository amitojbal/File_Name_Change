import datetime

#provide month number
month_num = "5"
datetime_object = datetime.datetime.strptime(month_num, "%m")

month_name = datetime_object.strftime("%b")
print("Short name: ",month_name)

full_month_name = datetime_object.strftime("%B")
print("Full name: ",full_month_name)