ticketPrice = int(input())
baggage = int(input())
if baggage > 0:
    weight = int(input())
    if weight >= 15:
        chargeRate = ticketPrice + weight * chargeRate
else:
    discount = 10
    finalPrice = ticketPrice - discount
print(finalPrice)