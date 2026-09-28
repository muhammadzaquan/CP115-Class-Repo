num_days = int(input())
danger_threshold = float(input())
danger_days = 0
total_temp = 0.0

for days in range(num_days):
    temperature = float(input())
    total_temp += temperature
    if temperature > danger_threshold:
        danger_days += 1
average_temp = total_temp / num_days

print(danger_days)
print(f"{average_temp:.1f}")
