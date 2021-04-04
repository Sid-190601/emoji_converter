def emoji_converter(message):
    words = message.split(" ")
    emojis ={
        ':)' : '😃',
        ':(' : '😔',
        '-_-': '😑',
        ':/' : '😕',
        '>_<': '😆'
    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    return output

message = input("Enter your message:")

print(emoji_converter(message))
