import os
from datetime import datetime as dt
os.chdir(r'C:\Users\amitoj\Downloads\File_Name_Change\Citi')

for f in os.listdir():

    f_txt_name, f_ext = os.path.splitext(f)

    f_month, f_day = f_txt_name.split(' ')

    f_month_name_num = dt.strptime(f_month, '%B')

    f_month_num = f_month_name_num.strftime("%m")

    # print(type(f_month_num))

    # f_date_str = '{}-{}-{}'.format(dt.now().year-f_month_num.month-f_day)

    f_yr = str(dt.now().year)
    f_mt = str(f_month_num)
    f_dt = str(f_day)

    f_date = str(f_yr + "-" + f_mt + "-" + f_dt)

    # print(f_date)
    # 'format'.format(("Amex") + filename + {Month} + {ext})
    new_name = '{}_{}_{}{}'.format(('Citi'), f_date, f_month, f_ext)

    # print(new_name)

    os.rename(f, new_name)