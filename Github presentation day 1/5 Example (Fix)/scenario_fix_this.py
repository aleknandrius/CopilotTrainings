import threading
import time

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        local = self.value
        time.sleep(0.01)
        self.value = local + 1

def run_threads():
    counter = Counter()
    threads = []
    for _ in range(100):
        t = threading.Thread(target=counter.increment)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Final counter value:", counter.value)


if __name__ == "__main__":
    # We expect 100, but often get something less due to race conditions
    run_threads()
