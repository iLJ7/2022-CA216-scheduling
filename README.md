I acknowledge and accept the DCU Academic Integrity and Plagiarism Policy for all of the submitted materials for assignment 1 (MyShell).
Name: Luke Whelan
Student ID: 20463814

Video: https://youtu.be/TUNnFglQvMo

PROGRAM USAGE:

Run FCFS, SJF and Priority algorithms like so:
python3 driver.py schedule.txt

where schedule.txt are the tasks to be run.

To run Round Robin too:
python3 driver.py schedule.txt rr_schedule.txt

where schedule.txt are the tasks for the FCFS, SJF
and Priority, and rr_schedule.txt are the tasks in the appropriate format for round robin.

NOTE: My round robin algorithm will support variable time quantums.
Thus, the format is:
[TaskName] [Quantum] [Burst]
