user_name = str(input("Enter your name: "))
class_name = str(input("Enter your class name: "))
subjects = str(input("Enter your subjects (comma-separated): ")).split(",")

print("User Name:", user_name)
print("Class:", class_name)
print("Subject(s):", ", ".join(subjects))