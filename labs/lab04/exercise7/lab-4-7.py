tempRoom = int(input())
tempTarget = int(input())
if tempTarget > tempRoom:
    power = tempTarget - tempRoom * 10
else:
    power = tempTarget + tempRoom * 8
if power > 100:
    power = 100
print(power)