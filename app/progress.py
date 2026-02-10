import time

def simulate_progress(callback, steps=100, delay=0.05):
    for i in range(steps + 1):
        callback(i)
        time.sleep(delay)