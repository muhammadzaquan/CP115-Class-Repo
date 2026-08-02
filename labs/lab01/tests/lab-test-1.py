weight = float(input())
if weight > 5:
    totalCharge = (5 * 8) + ((weight - 5) * 6)
    if totalCharge > 60:
        totalCharge = totalCharge + 10
else:
    totalCharge = weight * 8
print(weight)
print(totalCharge)