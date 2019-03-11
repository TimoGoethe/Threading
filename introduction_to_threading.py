"""Working with Threads

Three threads are a class and one thread is a function.
You are using sleep-statements to simulate processor-time.
It's all about running things in parallel."""


from threading import Thread, active_count, current_thread, enumerate
from time import sleep

# Do you want structural sleeps within the program?
structural_sleep = True
# Do you want any sleeps within the program? Enable or disable if need be
active_sleep = True
# disable to see what happends if there is no join... it will run until the end (6 minutes long)
enable_join = True
print("At the beginning,", active_count(), "Threads are active.\n")
# At the beginning, the main thread is always existing. If you're not using any thread-related
# modules, then you are programming with the main thread only.
# I don't know why there are 2 active threads at the beginning.
print("At the beginning, that's the current thread:", current_thread())

print("\nIs the current thread a demon-thread?", current_thread().isDaemon())
    
print("\nAt the beginning, these are all active threads:", enumerate())


class Thread1(Thread):
    def run(self):
        """it's important to name the function 'run'"""
        for i in range(5):
            print("This is Thread1")
            print("This statement stands in the class Thread1. What is the current_thread\
                  right now?", current_thread())


class Thread2(Thread):
    def run(self):
        for i in range(3):
            if active_sleep:
                sleep(2)
            print("This is Thread2")
            print("This statement stands in the class Thread2. What is the current_thread\
                  right now?", current_thread())


def thread3(a):
    for i in range(5):
        if active_sleep:
            sleep(1)
        print("This is thread3")
        print("This statement stands in the class thread3. What is the current_thread\
                  right now?", current_thread())


if active_sleep and structural_sleep:
    sleep(3)
print("\n\nWithout using threads, running the two classes and the function is a linear process.\n")
print("Now", active_count(), "Threads are active.\n")
print("What is the current_thread right now?", current_thread())
a1 = Thread1()
print("Now", active_count(), "Threads are active.\n")
a1.run()
print("Now", active_count(), "Threads are active.\n")
print("What is the current_thread right now?", current_thread())
a2 = Thread2()
print("Now", active_count(), "Threads are active.\n")
a2.run()
thread3(5) # I picked 5 randomly, the argument doesn't matter here
print("Now", active_count(), "Threads are active.\n")
if active_sleep and structural_sleep:
    sleep(3)

print("###############################################")
print("\n\nWith multithreading, the classes and functions run in parallel")
if active_sleep and structural_sleep:
    sleep(1)
print("Be careful, everything can be mixed up, because many things are running in parallel!")
print("You'll see mixed up print-statements in the following part")
if active_sleep and structural_sleep:
    sleep(1)

# classes and function can be used similarly after creating the objects t1, t2, t3
print("Now", active_count(), "Threads are active.\n")
print("What is the current_thread right now?", current_thread())
t1 = Thread1() 
print("Now", active_count(), "Threads are active.\n") 
t2 = Thread2()
print("Now", active_count(), "Threads are active.\n")
t3 = Thread(target=thread3, args=(5,))
print("Now", active_count(), "Threads are active.\n")
# Now everything is getting mixed up
print("What is the current_thread right now?", current_thread())
t1.start() # thread 1
print("Now", active_count(), "Threads are active.\n") # main-thread
print("What is the current_thread right now?", current_thread())
t2.start() # thread 2
print("Now", active_count(), "Threads are active.\n") # main-thread
print("What is the current_thread right now?", current_thread())
t3.start() # thread 3
print("Now", active_count(), "Threads are active.\n") # main-thread
print("Everything done")

if active_sleep and structural_sleep:
    sleep(3)
print("###############################################")
print("The join command is very helpful. Via default, you don't wait for all threads\
      to terminate. The program just goes on with the following statements and executes\
      them via main-thread. But maybe you need all threads to terminate before going on\
      with the main-thread. Use join to make them wait for the thread t, if you use t.join()\
      you can also add an argument to join, e.g. t.join(5). Then, all following commands are\
      only executed if thread t is done of if 5 seconds are over.")


class Thread4(Thread):
    def run(self):
        print("This is supposed to take super long")
        for i in range(120):
            if active_sleep:
                sleep(3)
            print("This is Thread4")


# t1.start() would generate a RuntimeError: threads can only be started once
# is t1 still running? Test it with t1.is_alive()
print("Is t1 still running?", t1.is_alive())
t1b = Thread1()
t1b.start()
t4 = Thread4()
t4.start()
if enable_join:
    # be aware: it's not threading.join, it's just join, no module name in front of the name
    t1b.join()
    t4.join(20)
if active_sleep:
    sleep(1)
print("##That's the following command##")

# Why does the program not terminate? 
