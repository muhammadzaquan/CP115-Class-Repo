import random
class_name = input("Enter your class names (comma-separated): ")
names = class_name.split(",")
random_name = random.choice(names)
print(f"{random_name} is the class of the day!")