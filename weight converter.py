weight = int(input('Hello. I am a weight converter. Can you tell me how much you weigh? '))
unit = input("Thank you. Now, can you tell me , is that in (Lbs) or (Kilos)? ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'''
Great. In kilos, you weigh {converted}''')
else:
    converted = weight // 0.45
    print(f'''
Great. In lbs, you weight {converted}''')

print('''
Now lose weight, fat ass.''')
