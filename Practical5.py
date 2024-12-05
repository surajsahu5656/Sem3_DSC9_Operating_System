""" Write a program to copy files using system calls. """

import shutil
def copy_files(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File {source} copied to {destination} file")
    except IOError as e:
        print(f"Error {e}")
source_file = "D:\Hemant kumar\h1.txt"
destination_file = "D:\Hemant kumar\h2.txt"

copy_files(source_file, destination_file)