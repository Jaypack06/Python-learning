import numpy as np
def calculate_daily_averages(temps):
    return np.mean(temps, axis=1)
def find_hottest_day(temps):
    return np.argmax(np.max(temps, axis=1))
def count_cold_readings(temps, threshold):
    return np.sum(temps < threshold)
    
    
def normalize_temperatures(temps):    
    min_temp = np.min(temps)
    max_temp = np.max(temps)
    normalized = (temps - min_temp) / (max_temp - min_temp) * 100
    return normalized

if __name__ == "__main__":
    temps = np.array([
        [65, 75, 70], # Day 0
        [68, 78, 72], # Day 1
        [70, 80, 75], # Day 2
        [62, 73, 68], # Day 3
        [67, 77, 71], # Day 4
        [69, 79, 74], # Day 5
        [64, 74, 69]  # Day 6
    ])
    
    print("Daily Averages:", calculate_daily_averages(temps))
    print("Hottest Day Index:", find_hottest_day(temps))
    print("Cold Readings (<70):", count_cold_readings(temps, 70))
    print("Normalized (first day):", normalize_temperatures(temps)[0])
    