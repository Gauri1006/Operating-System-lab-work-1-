processes = ["P1", "P2", "P3"]
brust = [5, 3, 8]

time = 0 

print("Processes\tCT\tTAT\tWT")

for i in range (len(processes)):
    time += brust[i]
    ct = time 
    tat = ct
    wt = tat-brust[i]
    print(processes[i], "\t", ct, "\t", tat, "\t", wt)
