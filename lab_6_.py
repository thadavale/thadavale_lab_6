# Tanushree Hadavale

# Lab 6 Encode Decode


encoded_numbers = []

def encode(decoded_numbers):
    global encoded_numbers
    for num in range(0, len(decoded_numbers)):
        new_num = int(num) + 4
        encoded_numbers.append(new_num)
    return encoded_numbers

user_input = input()
print(encode(user_input))