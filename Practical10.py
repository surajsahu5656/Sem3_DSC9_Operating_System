"""Write a program to implement SRJF scheduling algorithm. """

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def srjf_scheduling(processes):
    n = len(processes)
    time = 0
    completed = 0
    current_process = None
    while completed != n:
        # Find the process with the shortest remaining time at the current time
        shortest = None
        for process in processes:
            if process.arrival_time <= time and process.remaining_time > 0:
                if shortest is None or process.remaining_time < shortest.remaining_time:
                    shortest = process

        if shortest is not None:
            shortest.remaining_time -= 1
            time += 1

            if shortest.remaining_time == 0:
                shortest.completion_time = time
                shortest.turnaround_time = shortest.completion_time - shortest.arrival_time
                shortest.waiting_time = shortest.turnaround_time - shortest.burst_time
                completed += 1
        else:
            time += 1

    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.pid}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

# Sample process list
processes = [
    Process(1, 0, 7),
    Process(2, 2, 4),
    Process(3, 4, 1),
    Process(4, 5, 4)
]

srjf_scheduling(processes)
