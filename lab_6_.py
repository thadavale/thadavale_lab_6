# Tanushree Hadavale

# Lab 6 Encode Decode

encoded_numbers = []

def encode(decoded_numbers):
    global encoded_numbers
    for num in decoded_numbers:
        new_num = int(num) + 3                          # Adds 3 to every number in the decoded numbers list
        encoded_numbers.append(str(new_num))
    return encoded_numbers

