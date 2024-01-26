import numpy as np

total_waiting = 0
total_turn_around = 0

n_processes = int(input("Enter number of process: "))

arrival_time = np.empty(n_processes)
burst_time = np.empty(n_processes)
waiting_time = np.empty(n_processes)
turn_around_time = np.empty(n_processes)

print("Enter brust time and arrival time of the processes: ")
for i in range(n_processes):
    print(f"Process{i}:")
    burst_time[i] = float(input("Enter Burst time:"))
    arrival_time[i] = float(input("Enter Arrival time:"))

waiting_time[0] = 0
for i in range(1, n_processes):
    waiting_time[i] = waiting_time[i-1]+burst_time[i-1]+arrival_time[i-1]-arrival_time[i]

for i in range(n_processes):
    turn_around_time = waiting_time[i]+burst_time[i]

for i in range(n_processes):
    total_waiting += waiting_time[i]
    total_turn_around += turn_around_time[i]

avg_waiting = total_waiting/n_processes
avg_turn_around = total_turn_around/n_processes

print("Process\t\tBurst Time\tArrival Time\tWaiting Time\tTurn around time")
for i in range(n_processes):
    print((f"Process[{i}]:\t{burst_time[i]}\t\t\t{arrival_time[i]}"
    f"\t\t\t{waiting_time[i]}\t\t\t\t{turn_around_time[i]}"))

print(f"Average waiting time:{avg_waiting}\nAverage turn around time:{avg_turn_around}")