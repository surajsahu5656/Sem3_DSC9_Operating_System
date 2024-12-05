"""Write a program to report behavior of Linux kernel including kernel version, CPU type and model. (CPU information)"""

import os
import platform
import cpuinfo

def get_kernel_version():
    return platform.release()

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return info

def main():
    print("Linux Kernel Version:", get_kernel_version())
    cpu_info = get_cpu_info()
    print("CPU Type and Model:", cpu_info['brand_raw'])

if __name__ == "__main__":
    main()
