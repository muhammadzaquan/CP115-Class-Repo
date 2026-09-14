current_reading = int(input())
previous_reading = int(input())

if current_reading >= previous_reading:
    consumption = current_reading - previous_reading

if consumption <= 20:
    water_cost = consumption * 0.57
elif 20 < consumption <= 35:
    water_cost = consumption * 1.03
elif consumption > 35:
    water_cost = consumption * 1.4

total_bill = water_cost + 8 + 2

print(consumption)
print(water_cost)
print(total_bill)
