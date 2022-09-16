# I acknowledge and accept the DCU Academic Integrity and Plagiarism Policy for all of the submitted materials for assignment 1 (MyShell).
# Name: Luke Whelan
# Student ID: 20463814

import calcTurnAround

def run(processes, scheduler):

    print(f"{scheduler}:")

    if scheduler == "round-robin":
        total = 0

        for key in processes:
            print(f"Process {key} arrived at time 0 and ran for {processes[key][1]} units. It had a turn-around time of {processes[key][0]} units")
            total += processes[key][0]

        print(f'The average turn-around time for round-robin was {total / len(processes)} units')

    else:
        curr = 0
        for process in processes:

            name, priority, burst = process[0], process[1], process[2]
            turnAroundTimes = calcTurnAround.calcTurnAround(processes)

            print(f"Process {name} arrived at time 0 and ran for {burst} units. It had a turn-around time of {turnAroundTimes[curr]} units")

            curr += 1

        averageTAT = sum(turnAroundTimes) / len(turnAroundTimes)
        print(f"The average turn-around time for {scheduler} was {averageTAT} units")

    print("---")
