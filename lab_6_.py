# Tanushree Hadavale

# Lab 6 Encode Decode

encoded_numbers = []

def encode(decoded_numbers):
    global encoded_numbers
    for num in decoded_numbers:
        new_num = int(num) + 3                          # Adds 3 to every number in the decoded numbers list
        if new_num in range (7, 13):
            new_num = new_num % 10
        encoded_numbers.append(str(new_num))
    encoded_numbers = ''.join(encoded_numbers)
    return str(encoded_numbers)

input = input()

print(encode(input))

# Alice Jiang

def decode(encoded_pass):
    decoded_pass = ""
    for num in range(0, len(encoded_pass)):
        if int(encoded_pass[num]) - 3 < 0:
            decoded_num = str(10 + (int(encoded_pass[num])) - 3)
        else:
            decoded_num = str(int(encoded_pass[num]) - 3)
        decoded_pass += decoded_num
    return decoded_pass


