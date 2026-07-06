income = int(input())
if income >= 50000:
    if income >= 100000:
        incomeTax = 0.02
    else:
        incomeTax = 0.01
totalTax = income * incomeTax
print(totalTax)