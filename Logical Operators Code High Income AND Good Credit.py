 #Logical Operators. If one statement AND another statement are both true, then statement follows.
 #Example: If borrower has high income AND good credit, then they are eligible for a loan.
 #Note: Cal also use "or" operator, which means only one of the conditions needs to be true.

has_high_income = True
has_good_credit = True

if has_good_credit and has_high_income:
     print("You are eligible for a loan you lucky SOB")
else: print("You sorry son of a bitch. Get out!")
