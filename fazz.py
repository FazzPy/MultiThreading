from imp import reload
from pdb import Restart
import threading
import time

def func1():
    while True:
        i = 0
        while(i < 10):
            i = i + 1
            time.sleep(1)
            print("1. Döngü : ",i)
            if i > 10:
                reload()

def func2():
    while True:
        i = 0
        while(i < 10):
            i = i + 1
            time.sleep(1)
            print("2. Döngü : ", i)
            if i > 10:
                reload()

trd1 = threading.Thread(target=func1)
trd2 = threading.Thread(target=func2)
trd1.start()
trd2.start()