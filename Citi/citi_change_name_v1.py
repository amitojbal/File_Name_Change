import os 
import datetime

os.chdir(r'C:\Users\amitoj\Downloads\CreditCardStatements\Citi')

for f in os.listdir():

    f_txt_name, f_ext = os.path.splitext(f)
    
    f_date, f_month = f_txt_name.split(' ')
    
    # print(f_date, f_month_name)
    # f_year, f_month_num, f_day = f_date.split('-')
    
    
    # # #provide month number
    # month_num = f_month_num
    # datetime_object = datetime.datetime.strptime(month_num, "%m")

    # f_month_name = datetime_object.strftime("%B")

    # 'format'.format(("Amex") + filename + {Month} + {ext})
    new_name = '{}_{}_{}{}'.format(('Citi'), f_date, f_month , f_ext)
    # print(new_name)

    os.rename(f, new_name)