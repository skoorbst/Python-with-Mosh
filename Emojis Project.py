message = input ("> ")
words = message.split(' ')
emojis = {
    ":)": "😀",
    "::": "🤯",
    "robot": "🦾"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)