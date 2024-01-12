import random

print("Welcome to the Password generator\n")
qnt_letters = int(input("How many letters would you like in your password?\n"))
qnt_symbols = int(input("How many symbols would you like?\n"))
qnt_numbers = int(input("How many numbers would you like\n"))
alphabet = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X","x","Y","y", "Z", "z"]
symbols = ["^", "°", "!", "§", "$", "%", "&", "/", "{", "(", "[", ")", "]", "=", "}", "ß", "?", "\ ", "*", "-", "+", ",", ";", ".", ":", "_", "#"]
numbers = list(range(0, 10))


def PyPass():

    Pass_letters = random.sample(alphabet, qnt_letters)
    Pass_symbols = random.sample(symbols, qnt_symbols)
    Pass_numbers = random.sample(range(0, 10), qnt_numbers)
    pypass_structure = Pass_letters + Pass_numbers + Pass_symbols
    pypass_set = set(pypass_structure)
    pypass_list = list(pypass_set)
    pypass = ''.join(map(str, pypass_list))

    print("\n", pypass)


PyPass()
