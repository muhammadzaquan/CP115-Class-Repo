score = int(input())
total_a = 0
total_b = 0
i = 1

while score != -1:
    if i % 2 > 0:
        total_a += score
    else:
        total_b += score
    i += 1
    if total_a > total_b:
        winner = "A"
    elif total_b > total_a:
        winner = "B"
    elif total_a == total_b:
        winner = "Tie"
    score = int(input())




print(total_a)
print(total_b)
print(winner)
