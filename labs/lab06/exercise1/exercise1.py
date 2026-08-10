print("========== RECEIPT ==========")
print("\nItem\tPrice\tQty\tTotal\n")
item1 = Coffee = 3.50
qty = 2
total = float(item1 * qty)
print(f"Coffee\t$3.50\t{qty}\t${total:.2f}\n")
item2 = Muffin = 2.10
qty = 3
total = float(item2 * qty)
print(f"Muffin\t$2.10\t{qty}\t${total:.2f}\n")
item3 = Water = 1.05
qty = 4
total = float(item3* qty)
print(f"Water\t$1.05\t{qty}\t${total:.2f}\n")
print("------------------------------")
print(f"\nSubtotal:\t\t${(3.50*2)+(2.10*3)+(1.05*4):.2f}")
tax = ((3.50*2)+(2.10*3)+(1.05*4)) * 0.06
print(f"\nTax (6%)\t\t${tax:.2f}")
print(f"\nTotal:\t\t\t${((3.50*2)+(2.10*3)+(1.05*4))+tax:.2f}")
print("\n==============================")

