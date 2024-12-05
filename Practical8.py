"""Write a program to implement the SJF scheduling algorithm."""

class Process:
    def __init__(self, name, burst_time):
        self.name= name
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
def sjf(processes):

    shorted_processes= sorted(processes, key = lambda x : x.burst_time)
    total_turnaround_time = 0
    total_waiting_time = 0
    for i in range(len(shorted_processes)):
        if i ==0:
            shorted_processes[i].waiting_time =0
        else:
            shorted_processes[i].waiting_time = shorted_processes[i-1].waiting_time+ shorted_processes[i-1].burst_time
        shorted_processes[i].turnaround_time = shorted_processes[i].waiting_time + shorted_processes[i].burst_time
        total_turnaround_time += shorted_processes[i].turnaround_time
        total_waiting_time += shorted_processes[i].waiting_time
    for process in shorted_processes :
        print(f"Process: {process.name}, Waiting time { process.waiting_time}, Turnaound Time : {process.turnaround_time}")
    average_turnaround_time = total_turnaround_time/len(processes)
    average_waiting_time = total_waiting_time/len(processes)
    print("Average Turn Around time:", average_turnaround_time)
    print("Average Waiting time :", average_waiting_time)
processes_sjf = [
    Process("P1", 10),
    Process("P2", 5),
    Process("P3", 8),
    Process("P4", 4),
    Process("P5", 3)
]

sjf(processes_sjf)