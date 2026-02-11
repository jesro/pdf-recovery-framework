def estimate_time(letters, digits, speed=1000):
    """
    Estimate time in seconds.
    letters: number of letters
    digits: number of digits
    speed: attempts per second (simulation)
    """
    from math import pow
    total_combinations = pow(26, letters) * pow(10, digits)
    seconds = total_combinations / speed
    return seconds