import random

def generate_password():
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
           'v', 'b', 'n', 'm', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Q', 'W',
           'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '?', '/', ',', '|', '>', '<', '+', '=', '_']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    no_of_letters =random.randint(8,10)
    no_of_symbols =random.randint(2,4)
    no_of_numbers =random.randint(2,4)

    password_list = []
    password = ""
    for l in range(1, no_of_letters + 1):
        password_list += random.choice(letters)

    for s in range(1, no_of_symbols + 1):
        password_list += random.choice(symbols)

    for n in range(1, no_of_numbers + 1):
        password_list += random.choice(numbers)


    random.shuffle(password_list)
    password = ""
    for ch in password_list:
        password += ch
    return password
