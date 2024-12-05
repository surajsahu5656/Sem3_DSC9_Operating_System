"""Write a program to implement a non-preemptive priority based scheduling algorithm."""

class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_scheduling(processes):
    # Sort processes based on priority (lower number means higher priority)
    processes.sort(key=lambda x: x.priority)

    # Calculate waiting time for each process
    for i in range(1, len(processes)):
        processes[i].waiting_time = processes[i-1].waiting_time + processes[i-1].burst_time

    # Calculate turnaround time for each process
    for i in range(len(processes)):
        processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time

    # Print process scheduling result
    print("Process ID\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.pid}\t\t{process.burst_time}\t\t{process.priority}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

# Sample process list
processes = [
    Process(1, 10, 2),
    Process(2, 1, 1),
    Process(3, 2, 4),
    Process(4, 1, 3),
    Process(5, 5, 2)
]

priority_scheduling(processes)
