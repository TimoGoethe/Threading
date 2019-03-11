"""I'm trying to create a "problem" here by provocating mistakes in calculation...

   but my program always calculates the correct result -.-
   Any idea how to create a "problem"? k1.info should return anything other than 200
   even though I deposit and withdraw the same amount."""

from time import sleep
from threading import Thread, active_count, current_thread, enumerate
import multiprocessing

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        sleep(0.01)
        self.balance += amount

    def withdraw(self, amount):
        sleep(0.008)
        self.balance -= amount

    def info(self):
        print(self.balance)


k1 = BankAccount(200)


def changes1():
    for i in range(100):
        k1.deposit(10)
        sleep(0.009)
        print("You deposited 10")


def changes2():
    for i in range(100):
        k1.withdraw(10)
        sleep(0.005)
        print("You withdraw 10")


thread1 = Thread(target=changes1)
thread2 = Thread(target=changes2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
k1.info()

###################################################################################
print("####################################################################")
print("\n"*20)
sleep(3)
# The solution: using locks
def changes3(lock):
    for i in range(100):
        lock.acquire()
        k1.deposit(10)
        sleep(0.009)
        print("You deposited 10")
        lock.release()


def changes4(lock):
    for i in range(100):
        lock.acquire()
        k1.withdraw(10)
        sleep(0.005)
        print("You withdraw 10")
        lock.release()

lock = multiprocessing.Lock()
thread3 = Thread(target=changes3, args=(lock,))
thread4 = Thread(target=changes4, args=(lock,))
thread3.start()
thread4.start()
thread3.join()
thread4.join()
k1.info()
