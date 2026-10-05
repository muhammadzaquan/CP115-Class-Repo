found_number = 0

for number in range (1, 100):
    if number % 7 == 0 and number % 13 == 0:
        found_number = number
        break
    number += 1



print(found_number)
