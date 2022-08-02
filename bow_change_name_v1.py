import os 
from datetime import datetime as dt

os.chdir(r'C:\Users\amitoj\Downloads\File_Name_Change\BoW')

for f in os.listdir():
    f_rm_name, f_ext = os.path.splitext(f)

    f_rm, f_ch_date = f_rm_name.split(' ')
      
    dt_obj = dt.strptime(f_ch_date, '%m_%d_%y')

    f_month_name = dt_obj.strftime("%B")
    f_date = dt_obj.strftime('%Y-%m-%d')
        
    # 'format'.format(("Amex") + filename + {Month} + {ext})
    new_name = '{}_{}_{}{}'.format(('BoW'), f_date, f_month_name, f_ext)
    
    os.rename(f, new_name)