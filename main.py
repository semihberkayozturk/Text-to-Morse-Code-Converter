from time import sleep

user_text = input("Welcome to the text-based Python program that converts Strings into Morse Code.\nType your text: ")

converter = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'ç': '-.-..',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'ı': '..',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'ö': '---.',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    'ş':'.--..',
    't': '−',
    'u': '··−',
    'ü': '..--',
    'ğ': '--.-.',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

output = []

def converter_to_morse():
    for i in user_text:
        i = i.lower()
        output.append(converter[i])

converter_to_morse()
final = ''.join(output)

if len(user_text) < 50:
    print(f"The Morse code of '{user_text}' is {final}")
else:
    print("The AI is  converting your text into morse code. Please wait 2 seconds.")
    sleep(2)
    print(f"The Morse code of '{user_text}' is {final}")



