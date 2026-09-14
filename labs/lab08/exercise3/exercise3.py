day_type = input()
show_time = int(input())
customer_type = input()

if day_type == "weekend" and customer_type == "Adult":
    base_price = 18.00
elif day_type == "weekend" and customer_type == "Child":
    base_price = 12.00
elif day_type == "weekend" and customer_type == "Senior":
    base_price = 15.00
elif day_type == "weekday" and customer_type == "Adult":
    base_price = 15.00
elif day_type == "weekday" and customer_type == "Child":
    base_price = 10.00
elif day_type == "weekday" and customer_type == "Senior":
    base_price = 12.00

if show_time > 18:
    final_price = base_price + 3
else:
    final_price = base_price

print(base_price)
print(f"{final_price:.2f}")
