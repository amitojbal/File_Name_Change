import os 
import datetime

os.chdir(r'C:\Users\amitoj\Downloads\File_Name_Change\Amex')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    
    f_year, f_month_num, f_date = f_name.split('-')
    
    #provide month number
    month_num = f_month_num
    datetime_object = datetime.datetime.strptime(month_num, "%m")

    f_month_name = datetime_object.strftime("%B")

    # 'format'.format(("Amex") + filename + {Month} + {ext})
    new_name = '{}_{}_{}{}'.format(('Amex'), f_name, f_month_name, f_ext)

    os.rename(f, new_name)