from time import sleep, time
import threading

#Wrong answer
def setTimeout(f, n=1000):
    n = n/1000
    sleep(n)
    f()

#Correct answer
class Scheduler:
    def __init__(self):
        self.fns = []
        t = threading.Thread(target=self.poll)
        t.start()
    
    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now >= due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)
    
    def delay(self, f, n):
        self.fns.append((f, time()*1000 + n))