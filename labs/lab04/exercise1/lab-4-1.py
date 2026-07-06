kwh = int(input())
if kwh >= 100:
    if kwh >= 200:
        chargeRate = 0.75
    else:
        chargeRate = 0.5
else:
    chargeRate = 0.3
totalBill = kwh * chargeRate
print(totalBill)