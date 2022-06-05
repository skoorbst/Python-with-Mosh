#New car costs €10000. If good credit, down payment on car is 10% (€1000). Otherwise, down payment is €2000.

new_car_price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = new_car_price * 0.1
else:
    down_payment = new_car_price * 0.2
print(f"The down payment on your new car is {down_payment}")