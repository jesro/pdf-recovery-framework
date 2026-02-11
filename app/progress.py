import time

def simulate_progress(total=100, interval=0.05):
    """
    Generator to simulate progress (0-100)
    """
    for i in range(total+1):
        yield i
        time.sleep(interval)