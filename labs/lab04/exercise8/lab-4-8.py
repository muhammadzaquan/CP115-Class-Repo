distance = float(input())
afterMidnight = (input().lower == 'true')
fare = 4
if distance >= 2:
    fare = fare + distance - 2 * 1.2
    if afterMidnight:
        fare = fare + 3
else:
    if afterMidnight:
        fare = fare + 3
print(fare)