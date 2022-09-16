# I acknowledge and accept the DCU Academic Integrity and Plagiarism Policy for all of the submitted materials for assignment 1 (MyShell).
# Name: Luke Whelan
# Student ID: 20463814

import sys
import fileRead
import scheduler, rr_scheduler

def main():
    rawList = fileRead.fileReader(sys.argv[1])
    scheduler.schedule(rawList)

    # If there are 3 arguments, then a round robin schedule text file has been given.
    # So, we call the round robin scheduler on the rr schedule text file.
    if len(sys.argv) == 3:
        rawListRR = fileRead.fileReader(sys.argv[2])
        rr_scheduler.schedule(rawListRR)

if __name__ == "__main__":
    main()
