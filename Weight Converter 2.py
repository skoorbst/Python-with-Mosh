weight = int(input("Hi. How much do you weigh? "))
unit = input("Is that in (L)bs or in (K)g? ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You weigh {converted} in kilos")
else:
    converted = weight // 0.45
    print(f"You weight {converted} in lbs")