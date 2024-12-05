"""Write a program to implement FCFS scheduling algorithm."""

def fcfs_scheduling(processes, arrival_time, burst_time):
    n = len(processes)
    # Initialize variables
    completion_time = [0] * n
    turn_around_time = [0] * n
    waiting_time = [0] * n
    
    # Sort processes by arrival time (if not already sorted)
    processes_sorted = sorted(zip(arrival_time, burst_time, processes), key=lambda x: x[0])
    arrival_time = [x[0] for x in processes_sorted]
    burst_time = [x[1] for x in processes_sorted]
    processes = [x[2] for x in processes_sorted]
    
    # Calculate completion time
    for i in range(n):
        if i == 0:
            completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            completion_time[i] = max(completion_time[i-1], arrival_time[i]) + burst_time[i]
    
    # Calculate Turn Around Time and Waiting Time
    for i in range(n):
        turn_around_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turn_around_time[i] - burst_time[i]
    
    # Display Results
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurn Around Time\tWaiting Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{turn_around_time[i]}\t\t{waiting_time[i]}")
    
    # Average Turn Around Time and Waiting Time
    avg_tat = sum(turn_around_time) / n
    avg_wt = sum(waiting_time) / n
    print(f"\nAverage Turn Around Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


# Input Data
processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 1, 2, 3]  # Arrival times for each process
burst_time = [5, 3, 8, 6]   # Burst times for each process

# Call the function
fcfs_scheduling(processes, arrival_time, burst_time)
