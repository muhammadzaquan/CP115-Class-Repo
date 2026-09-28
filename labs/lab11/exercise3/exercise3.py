number = int(input())
count = 0
biggest_jump = 0
jump = 0
previous_number = number

while number != 0:
    jump = number - previous_number
    if jump > biggest_jump:
        biggest_jump = jump
    previous_number = number
    count += 1
    number = int(input())
        
    




print(count)
print(biggest_jump)
