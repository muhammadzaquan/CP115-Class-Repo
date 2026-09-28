sales = int(input())
count = 0
record_days = 0
records = 0

while sales != 0:
    if sales > records:
        records = sales
        record_days += 1
    count += 1
    sales = int(input())

print(count)
print(record_days)
