speed = int(input())
total_readings = 0
streak = 0
longest_streak = 0

while speed != -1:
    if speed < 20:
        streak += 1
    
    else:
        streak = 0
    if streak > longest_streak:
                longest_streak = streak
    total_readings += 1
    speed = int(input())

print(total_readings)
print(longest_streak)
