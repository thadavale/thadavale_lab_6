# Tanushree Hadavale

# Lab 6 Encode Decode

def encode(decoded_numbers):
    encoded_numbers = []
    global encoded_numbers
    for num in decoded_numbers:
        new_num = int(num) + 3                          # Adds 3 to every number in the decoded numbers list
        if new_num in range (7, 13):
            new_num = new_num % 10
        encoded_numbers.append(str(new_num))
    encoded_numbers = ''.join(encoded_numbers)
    return str(encoded_numbers)


# Main Function
if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        user_input = input("Please enter an option: ")
        print()
        if user_input == "1":
            decoded_numbers = input("Please enter your password to encode: ")
            encoded_numbers = encode(decoded_numbers)
            print("Your password has been encoded and stored!")
            print()
        if user_input == "2":
            decoded_numbers = decode(encoded_numbers)
            print(f"The encoded password is {encoded_numbers}, and the original password is {decoded_numbers}.")
        if user_input == "3":
            break

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


