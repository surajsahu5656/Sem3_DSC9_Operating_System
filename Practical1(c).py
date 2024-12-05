"""Write a program (using fork() and/or exec() commands) where parent and child execute: 
c) Before terminating, the parent waits for the child to finish its task. """

import multiprocessing
import time

def child_process():
    print("Child process executing")
    time.sleep(2)
    print("Child process done")

def parent_process():
    print("Parent process executing")
    child = multiprocessing.Process(target=child_process)
    child.start()
    child.join()  # Wait for the child process to finish
    print("Child process finished")

if __name__ == "__main__":
    parent_process()
