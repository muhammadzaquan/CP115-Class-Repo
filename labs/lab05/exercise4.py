item_name = str(input("Enter the item name: "))
item_price = float(input("Enter the item price: "))
quantity = int(input("Enter the quantity: "))
if quantity > 3:
    tax_rate = 0.06
    subtotal = item_price * quantity + (item_price * quantity * tax_rate)
else:
    subtotal = item_price * quantity
print(f"Item: {item_name}, Price: {item_price}, Quantity: {quantity}, Subtotal: {subtotal:.2f}")
