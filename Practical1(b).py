"""Write a program (using fork() and/or exec() commands) where parent and child execute:  
b) Same program, different code. """

import os
import multiprocessing

def parent_task():
    print("Parent executing with its own code.")

def child_task():
    print("Child executing with its own code.")

if __name__ == "__main__":
    print("Parent executing same program with different code.")

    # Create a child process
    child_process = multiprocessing.Process(target=child_task)
    child_process.start()
    child_process.join()  # Wait for the child process to finish

    # Execute parent's task
    parent_task()
