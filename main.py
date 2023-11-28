from morse_dict import *

dict = MORSE_DICT

input_string = input('Enter your string:')
def decode_morse_code(morse_string, input_list):
    words = input_string.split(' ')
    decoded_message = ''
    for word in words:
        if word in input_list.values():
            decoded_message += list(input_list.keys())[list(input_list.values()).index(word)]
        else:
            return "Unsupported symbol in string"
    return decoded_message
decoded_message = decode_morse_code(input_string, dict)

print("Message:", decoded_message)



