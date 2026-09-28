num_rounds = int(input())
final_score = 0.0
rounds_processed = 0

for rounds in range(num_rounds):
    score = int(input())
    rounds_processed += 1

    if score > 100:
        bonus = score * 0.2
        final_score += score + bonus
    else:
        final_score += score

print(f"{final_score:.1f}")
print(rounds_processed)
