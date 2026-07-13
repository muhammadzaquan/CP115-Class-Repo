minutesBefore = int(input())
membership = (input().lower == 'true')
price = 80
if minutesBefore > 30:
    if minutesBefore > 0:
        if membership:
            price = price - price * 0.15
    else:
        price = price - 80
else:
    price = price - 15
    if membership:
        price = price - price * 0.15
print(price)