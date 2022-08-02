import os 
from datetime import datetime as dt

os.chdir(r'C:\Users\amitoj\Downloads\File_Name_Change\Patelco')

for f in os.listdir():

    f_txt_name, f_ext = os.path.splitext(f)

    # 'format'.format(("Amex") + filename + {Month} + {ext})
    new_name = '{}_{}_{}{}'.format(("Patelco"), ("2022-07-25"), ("July") , f_ext)
    # print(new_name)

    os.rename(f, new_name)