hours = int(input())
if hours >= 2:
    if hours >= 5:
        chargeRate = 3
    else:
        chargeRate = 2
parkingFee = hours * chargeRate
if parkingFee >30:
    parkingFee = 30
print(parkingFee)