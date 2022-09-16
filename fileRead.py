# I acknowledge and accept the DCU Academic Integrity and Plagiarism Policy for all of the submitted materials for assignment 1 (MyShell).
# Name: Luke Whelan
# Student ID: 20463814

# We read the lines in our file and add them to our initial processes list. Then, we return the list.

def fileReader(f):

    processes = []

    with open(f, 'r') as f:

        for x in f.readlines():
            x = x.replace(',', " ")
            x = x.strip().split()
            processes.append(x)

        return processes
