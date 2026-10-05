grade = float(input())
valid_count = 0
total = 0
average = 0.0

while grade != -1:

    grade = float(input())

    if grade < 0:
        continue
    if grade > 100:
        continue

    valid_count += 1
    total += grade
average = total / valid_count

print(valid_count)
print(f"{average:.2f}")
