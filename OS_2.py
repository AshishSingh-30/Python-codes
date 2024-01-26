bt = []
wt = []
avg_wt = 0
tat = []
avg_tat = 0
print("Enter the number of processes : ")
n = int(input())
print("Enter the burst time of the processes : ")
bt = list(map(int, input().split()))
wt.insert(0, 0)
tat.insert(0, bt[0])
for i in range(1, len(bt)):
    wt.insert(i, wt[i-1]+bt[i-1])
    tat.insert(i, wt[i]+bt[i])
    avg_wt += wt[i]
    avg_tat += tat[i]
avg_wt = float(avg_wt)/n
avg_tat = float(avg_tat)/n
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0, n):
    print(str(i)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
    print("\n")
print("Average Waiting time is: "+str(avg_wt))
print("Average Turn Around Time is: "+str(avg_tat))
