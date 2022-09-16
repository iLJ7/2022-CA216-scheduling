# I acknowledge and accept the DCU Academic Integrity and Plagiarism Policy for all of the submitted materials for assignment 1 (MyShell).
# Name: Luke Whelan
# Student ID: 20463814

import CPU
import time
import schedule_rr

def schedule(rawListRR):

    # We run he round-robin algorithm
    CPU.run(schedule_rr.schedule_rr(rawListRR), "round-robin")
