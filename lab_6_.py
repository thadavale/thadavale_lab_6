# Tanushree Hadavale

# Lab 6 Encode Decode

encoded_numbers = []

def encode(decoded_numbers):
    global encoded_numbers
    for num in range(1, len(decoded_numbers) + 1):
        new_num = int(num) + 3
        encoded_numbers.append(new_num)
    return encoded_numbers


