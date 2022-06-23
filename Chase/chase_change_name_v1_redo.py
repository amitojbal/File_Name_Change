import os 
import datetime

os.chdir(r'C:\Users\amitoj\Downloads\CreditCardStatements\Chase')

for f in os.listdir():

    f_txt_name, f_ext = os.path.splitext(f)
    
    f_name, f_date, f_month = f_txt_name.split('_')
    
    
    # f_year, f_month_num, f_day = f_date.split('-')
    
    

    
    # #provide month number
    # month_num = f_month_num
    # datetime_object = datetime.datetime.strptime(month_num, "%m")

    # f_month_name = datetime_object.strftime("%B")

    # 'format'.format(("Amex") + filename + {Month} + {ext})
    new_name = '{}_{}_{}{}'.format(('Chase'), f_date, f_month , f_ext)

    os.rename(f, new_name)