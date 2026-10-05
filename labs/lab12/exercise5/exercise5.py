number = int(input())
score = 0
ignored = 0
prev_number = number

while number != 0:

    number = int(input())
    if number > 0:
        previous_number = number
    if number <= prev_number:
        ignored += 1
        continue
    score += number
    prev_number = number

print(score)
print(ignored)
