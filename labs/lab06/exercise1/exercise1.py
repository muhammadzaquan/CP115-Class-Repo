def get_quantity(item):
	return int(input(f"Enter the quantity of {item}: "))


menu = {}
print("Create your menu. Press Enter without an item name when finished.")
while True:
	item = input("Enter an item name: ").strip()
	if not item:
		break
	menu[item] = float(input(f"Enter the price of {item}: $"))

orders = []
for item, price in menu.items():
	qty = get_quantity(item)
	total = price * qty
	orders.append((item, price, qty, total))

subtotal = sum(order[3] for order in orders)
tax = subtotal * 0.06

print(f"""========== RECEIPT ==========

Item\tPrice\tQty\tTotal

{''.join(f'{item}\t${price:.2f}\t{qty}\t${total:.2f}\n\n' for item, price, qty, total in orders)}

------------------------------

Subtotal:\t\t${subtotal:.2f}

Tax (6%)\t\t${tax:.2f}

Total:\t\t\t${subtotal + tax:.2f}

==============================""")

