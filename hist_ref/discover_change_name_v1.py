import os 
from datetime import datetime as dt

os.chdir(r'C:\Users\amitoj\Downloads\File_Name_Change\Discover')

for f in os.listdir():

    f_txt_name, f_ext = os.path.splitext(f)

    f_date_convert, f_month = f_txt_name.split(' ')

    f_date = dt.strptime(f_date_convert, '%Y-%m-%d')

    # print(f_date.date())

    # print(f_bank_name, f_date_convert, f_month)
    # print(f_date, f_month_name)
    # f_year, f_month_num, f_day = f_date.split('-')
    
    
    # # #provide month number
    # month_num = f_month_num
    # datetime_object = datetime.datetime.strptime(month_num, "%m")

    # f_month_name = datetime_object.strftime("%B")

    # 'format'.format(("Amex") + filename + {Month} + {ext})
    new_name = '{}_{}_{}{}'.format(('Discover'), f_date.date(), f_month , f_ext)
    # print(new_name)

    os.rename(f, new_name)