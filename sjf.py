processes = [ "P1", "P2", "P3"]
burst = [5, 3, 8]

for i in range(len(burst)):
    for j in range (i + 1, len(burst)):
        if burst[i] > burst[j]:
            burst[i], burst[j] = burst[j], burst[i]
            processes[i], processes[j] = processes[j], processes[i]

time = 0

print("processes\tBT\tCT\tTAT\tWT")

for i in range(len(processes)):
    time += burst[i]
    ct = time
    tat = ct
    wt = tat - burst[i]

    print(processes[i], "\t", burst[i], "\t", ct, "\t", tat, "\t", wt)
