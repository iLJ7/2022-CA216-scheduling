# I acknowledge and accept the DCU Academic Integrity and Plagiarism Policy for all of the submitted materials for assignment 1 (MyShell).
# Name: Luke Whelan
# Student ID: 20463814

# We sort the process list based on the value at index 2. I.e. based on the burst time given in our schedule.txt file.
# We utilise the lamba function to avoid having to manually sort all the entries with a sorting algorithm like selection / bubble sort.

def schedule_sjf(processes):
    processes = sorted(processes, key=lambda x:int(x[2]))

    return processes
