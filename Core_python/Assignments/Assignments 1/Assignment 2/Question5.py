#5. WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter cost price of book: "))
discount = float(input("Enter discount (%): "))

selling_price = cost_price - (cost_price * discount / 100)

print("Selling Price =", selling_price)
