from morse_dict import *

input_string = input('Enter your string:')
def decode_morse_code(morse_string, input_list):
    words = input_string.split(' ')
    decoded_message = ''
    for word in words:
        if word in morse_dict.values():
            decoded_message += list(morse_dict.keys())[list(morse_dict.values()).index(word)]
        else:
            return "Unsupported symbol in string"
    return decoded_message
decoded_message = decode_morse_code(input_string, morse_dict)

print("Message:", decoded_message)



