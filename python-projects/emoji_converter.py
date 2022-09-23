
def emoji_converter(emojis_dict):
    message = input('>')
    output = ''
    words = message.split(' ')
    for word in words :
     output += emojis.get(word, word) + " "
    print(output)


emojis = {
    ":)": "😀",
    ":(": "☹️"
}

emoji_converter(emojis)

