#Price of a house of €1 million.
#If buyer has good credit, they need to put down 10%.
#Otherwise, the down payment is 20%.

price_of_house = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price_of_house
else:
    down_payment = 0.2 * price_of_house
print(f"Down payment: {down_payment}")
