from threading import*
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            #sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            #sleep(1)

t1=Hello()
t2=Hi()
t1.start()
t2.start()
