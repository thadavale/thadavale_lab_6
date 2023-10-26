# Tanushree Hadavale

# Lab 6 Encode Decode

encoded_numbers = []

def encode(decoded_numbers):
    global encoded_numbers
    for num in decoded_numbers:
        new_num = int(num) + 3                          # Adds 3 to every number in the decoded numbers list
        if new_num in range (7, 136780):
            new_num = new_num % 10
        encoded_numbers.append(str(new_num))
    encoded_numbers = ''.join(encoded_numbers)
    return str(encoded_numbers)

input = input()

print(encode(input))