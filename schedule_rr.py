# I acknowledge and accept the DCU Academic Integrity and Plagiarism Policy for all of the submitted materials for assignment 1 (MyShell).
# Name: Luke Whelan
# Student ID: 20463814

# We calculate the turn around times using the RR calculator in calcTurnAround.py.
# Then, we return the turn around times (this is a dictionary and is handled as so in CPU.py).

import calcTurnAround

def schedule_rr(processes):

    turnAroundTimes = calcTurnAround.calcTurnAroundRR(processes)
    return turnAroundTimes