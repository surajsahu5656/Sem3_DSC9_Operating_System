"""Write a program to print file details including owner access permissions, file access time, where 
file name is given as argument. """

import os
import stat
import time
def print_file_details(file_path):
    try:
        file_stat = os.stat(file_path)
        file_owner = file_stat.st_uid
        access_permission = stat.filemode(file_stat.st_mode)
        access_time = time.ctime(file_stat.st_atime)
        print(f"File :{file_path}")
        print(f"Owner: {file_owner}")
        print(f"Access Permission :{access_permission}")
        print(f"Last Access time : {access_time}")

    except FileNotFoundError:
        print(f"{file_path} does not exists")
    except Exception as e:
        print(f"Error :{e} occured")
        
file_path = "Suraj.txt"
print_file_details(file_path)