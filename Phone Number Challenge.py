phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six"
}
output = ""
for ch in phone:
   output += digits_mapping.get(ch, "!") + " "
print(output)
