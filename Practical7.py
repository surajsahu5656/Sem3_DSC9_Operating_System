"""Write a program to implement Optimal scheduling algorithm."""

class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0

def optimal_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0

    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time

        process.start_time = current_time
        process.completion_time = current_time + process.burst_time
        current_time = process.completion_time

def print_schedule(processes):
    print("Process\tArrival Time\tBurst Time\tStart Time\tCompletion Time")
    for process in processes:
        print(f"{process.process_id}\t\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.start_time}\t\t{process.completion_time}")

def main():
    processes = [
        Process(1, 0, 5),
        Process(2, 2, 3),
        Process(3, 4, 8),
        Process(4, 7, 2),
    ]

    optimal_scheduling(processes)
    print_schedule(processes)

if __name__ == "__main__":
    main()
