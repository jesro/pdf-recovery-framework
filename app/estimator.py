def estimate(letters, digits, cpu_rate, gpu_rate):
    combos = (26 ** letters) * (10 ** digits)
    cpu_time = combos / cpu_rate
    gpu_time = combos / gpu_rate

    return {
        "combinations": combos,
        "cpu_seconds": int(cpu_time),
        "gpu_seconds": int(gpu_time)
    }