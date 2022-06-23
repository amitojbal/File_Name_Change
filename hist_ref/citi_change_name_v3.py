import os
from datetime import datetime as dt
from traceback import print_tb
import dateutil.parser
from pendulum import today

os.chdir(r'C:\Users\amitoj\Downloads\File_Name_Change\Citi')

for f in os.listdir():

    f_txt_name, f_ext = os.path.splitext(f)

    f_date_month = str(f_txt_name[0:4])
    f_date_day = f_txt_name[5:]

    print(f_date_month)
    print(f_date_day)

    # datetime_object = dt.strptime(f_date_month, "%b")

    # f_month = datetime_object.strftime("%m")
    # print("Full name: ",f_month)

    # f_date_month, f_date_day = f_txt_name.split(' ')

    # print(f_date_month, f_date_day)
     
    # f_date = dt.strptime(f_date_str, '%B %d %Y')

    # print(f_date)

    # f_date = dateutil.parser.parse(f_txt_name, '%B %d')
    
    # print(f_date)
    
    # f_date_str = '{}-{}'.format(f_txt_name, dt.now().year)

    # print(f_date_str)
    
    # 'format'.format(("Amex") + filename + {Month} + {ext})
    # new_name = '{}_{}_{}{}'.format(('Citi'), dt.now().year-f_date_month-f_date_day, f_ext)
    
    # print(new_name)

    # os.rename(f, new_name)
