minutes = int(input("Enter time in minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Original minutes: {minutes}")
print(f"Converted time: {hours} hour(s) and {remaining_minutes} minute(s)")
