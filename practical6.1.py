


def fcfs(processes, bt, arrival_time):
    n = len(processes)
    wt = [0] * n
    time=0
    starting_time=[0]*n
    tat=[0]*n
    ct=[0]*n
    for i in range(n):
        starting_time[i]=max(time,arrival_time[i])
        time=starting_time[i]+bt[i]
        ct[i]=time
        tat[i]=time-arrival_time[i]
        wt[i]=tat[i]-bt[i]
    avg_tat=sum(tat)/n
    avg_wt=sum(wt)/n
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{bt[i]}\t{wt[i]}\t{tat[i]}")
    print("avg of tat",avg_tat)
    print("avg of wt",avg_wt)
n=int(input("enter the number of processes"))
processes=[input(f"for process {i+1}" ) for i in range(n)]
arrival_time=[int(input(f"arrival time for process {i+1}")) for i in range(n)]
bt=[int(input(f"burst time for process {i+1}")) for i in range(n)]
fcfs(processes, bt, arrival_time)