# I acknowledge and accept the DCU Academic Integrity and Plagiarism Policy for all of the submitted materials for assignment 1 (MyShell).
# Name: Luke Whelan
# Student ID: 20463814

# Our function to calculate the turnaround time of a list of processes.
# They're already sorted, so we simply add the bursts.

def calcTurnAround(processes):

    turnAroundTimes = []
    bursts = []

    for i in range(0, len(processes)):
        burst = int(processes[i][2])

        turnAround = sum(bursts) + burst
        bursts.append(burst)
        turnAroundTimes.append(turnAround)

    return turnAroundTimes

# Our Round Robin turn-around time calculation will return a dictionary.
# The dictionary maps task names to turn around times and total burst time.
# The code below is arguably verbose, but it does the job well.

def calcTurnAroundRR(processes):

    bursts = []

    for process in processes:
        bursts.append(int(process[2]))

    remainders = []
    completeBursts = []
    quantums = []
    names = []

    for i in range(0, len(processes)):

        name = processes[i][0]
        burst = int(processes[i][2])
        quantum = int(processes[i][1])

        # If the burst is bigger than the quantum...
        if burst > quantum:
            noOfCompleteBursts = burst // quantum
            remainder = burst % quantum
        
        # Else, if the burst is less than or equal to the quantum...
        else:
            noOfCompleteBursts = 1
            remainder = 0
        
        remainders.append(remainder)

        completeBursts.append(noOfCompleteBursts)
        names.append(name)

        quantums.append(quantum)


    schedule = []

    completeBurstsCopy = []

    for burst in completeBursts:
        completeBurstsCopy.append(burst)

    nameSchedule = []

    while(completeBursts.count(-1) != len(completeBursts)):
        for i in range(0, len(completeBursts)):
            if completeBursts[i] > 0:
                schedule.append(quantums[i])
                completeBursts[i] -= 1
            
            else:
                schedule.append(remainders[i])
                completeBursts[i] -= 1
            
            nameSchedule.append(names[i])

    map = {}
    i = len(nameSchedule) - 1

    TATs = []
    while(i >= 0):
       TATs.append(sum(schedule[:i + 1]))
       i = i - 1

    quantum = quantums[i]
    for i in range(0, len(schedule)):
        if schedule[i] < quantum:
            target = i
            break
    
    TATs.reverse()
    TATs = TATs[target:]

    i = 0
    seen = []

    counter = 0
    while len(names) != len(seen):
        seen.append(nameSchedule[i])
        map[nameSchedule[i]] = [TATs[counter], bursts[counter]]
        counter += 1
        i = i + 1

    return map
