
def emoji_converter(input_message):
    try:
        emojis = {
            ":)": "😀",
            ":(": "☹️"
        }
        output = ''
        words = message.split(' ')
        for word in words:
            output += emojis.get(word, word) + " "
    except ValueError:
        output = 'Invalid Value'

    return output


def square(number):
    return number * number



message = input('>')
converted = emoji_converter(message)
squared = square(4)

