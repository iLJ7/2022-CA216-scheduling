import CPU
import time
import schedule_sjf, schedule_priority, schedule_fcfs

def schedule(rawList):
    # Our processes are FCFS sorted by default.

    print("This is the CA216 - Scheduling assignment submission for Luke Whelan (20463814)")
    time.sleep(5)
    print("The scheduler will now run and display the turn-around times for: ")
    time.sleep(3)
    print("First-Come-First-Served (fcfs)")
    time.sleep(1)
    print("Shortest-Job-First (SJF)")
    time.sleep(1)
    print("Priority")
    time.sleep(1)
    print("Robin-Robin (round-robin)")
    time.sleep(3)

    # We run the FCFS algorithm
    CPU.run(schedule_fcfs.schedule_fcfs(rawList), "fcfs")

    time.sleep(5)
    # We run the SJF-sorted algorithm
    CPU.run(schedule_sjf.schedule_sjf(rawList), "sjf")

    time.sleep(5)
    # We run the priority-sorted algorithm
    CPU.run(schedule_priority.schedule_priority(rawList), "priority")

    time.sleep(5)