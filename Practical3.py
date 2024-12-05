""" Write a program to report behavior of Linux kernel including information on configured memory, amount of free and used memory. (Memory information) """

import os
import platform
import psutil

def get_kernel_version():
    return platform.release()

def get_memory_info():
    memory = psutil.virtual_memory()
    total_memory = memory.total
    available_memory = memory.available
    used_memory = memory.used
    free_memory = memory.free
    
    return total_memory, available_memory, used_memory, free_memory

def main():
    print("Linux Kernel Version:", get_kernel_version())
    
    total_memory, available_memory, used_memory, free_memory = get_memory_info()
    print("Total Configured Memory:", total_memory // (1024 ** 2), "MB")
    print("Available Memory:", available_memory // (1024 ** 2), "MB")
    print("Used Memory:", used_memory // (1024 ** 2), "MB")
    print("Free Memory:", free_memory // (1024 ** 2), "MB")

if __name__ == "__main__":
    main()
