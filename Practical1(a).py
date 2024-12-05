"""Write a program (using fork() and/or exec() commands) where parent and child execute:  
a) Same program, same code. """

import multiprocessing

def child_process():
    print("Child executing same program with same code.")

def main():
    process = multiprocessing.Process(target=child_process)
    process.start()
    process.join()
    print("Parent executing same program with same code.")

if __name__ == "__main__":
    main()
