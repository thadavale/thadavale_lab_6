def decode(encoded_pass):
    decoded_pass = ""
    for num in range(0, len(encoded_pass)):
        decoded_num = str(int(encoded_pass[num]) - 3)
        decoded_pass += decoded_num
    return decoded_pass

