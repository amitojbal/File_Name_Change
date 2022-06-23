import os 
from datetime import datetime as dt

os.chdir(r'C:\Users\amitoj\Downloads\CreditCardStatements\Patelco')

for f in os.listdir():

    f_txt_name, f_ext = os.path.splitext(f)

    f_date_str = str(f_txt_name[0:8])
    f_month = f_txt_name[8:]

        
    f_date = dt.strptime(f_date_str, '%m%d%Y')

    # print(f_date.date())

    # # f_year, f_month_num, f_day = f_date.split('-')
    # # print(f_date.date(), f_date.month)
    
    # #provide month number
    # month_num = str(f_date.month)
    
    # datetime_object = dt.strptime(month_num, "%m")

    # f_month = datetime_object.strftime("%B")

    # # print(f_month_name)

    # 'format'.format(("Amex") + filename + {Month} + {ext})
    new_name = '{}_{}_{}{}'.format(("Patelco"), f_date.date(), f_month , f_ext)
    # print(new_name)

    os.rename(f, new_name)