"""Working with Threads

Three threads are a class and one thread is a function.
You are using sleep-statements to simulate processor-time.
It's all about running things in parallel."""

from threading import Thread, active_count, current_thread, enumerate
from time import sleep
import multiprocessing


class Thread1(Thread):
    def run(self):
        """it's important to name the function 'run'"""
        for i in range(100):
            sleep(0.001)
            print("This is Thread1")


class Thread2(Thread):
    def run(self):
        for i in range(100):
            sleep(0.00095)
            print("This is Thread2")


def thread3(a):
    for i in range(100):
        sleep(0.0009)
        print("This is thread3")


t1 = Thread1()
t2 = Thread2()
t3 = Thread(target=thread3, args=(5,))
t1.start()  # thread 1
t2.start()  # thread 2
t3.start()  # thread 3


