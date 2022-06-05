#Price of a house of €1 million.
#If buyer has good credit, they need to put down 10%.
#Otherwise, the down payment is 20%.

price_of_house = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price_of_house * 0.1
else:
    down_payment = price_of_house * 0.2
print(f"Your down payment is {down_payment}")



