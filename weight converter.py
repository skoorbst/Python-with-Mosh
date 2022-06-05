weight = int(input("Hi there, I am a weight converter. How much do you weigh? "))
unit = input("Thanks. Can you tell me if that is in (Lbs) or (Kilos)? ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Okay, thanks. Your wieght in kilos is {converted}")
else:
    converted = weight // 0.45
    print(f"Okay, thanks. Your weight in lbs is {converted}")

print('''
Now go get on a treadmill and stop eating Doritos!''')
