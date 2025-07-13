# binární strom.py
tree = {

    "A": "0",

    "B": "1",

    "C": "00",

    "D": "01",

    "E": "10",

    "F": "11",

    "G": "000",

    "H": "001",

    "I": "010",

    "J": "011",

    "K": "100",

    "L": "101",

    "M": "110",

    "N": "111",

    "O": "0000",

    "P": "0001",

    "Q": "0010",

    "R": "0011",

    "S": "0100",

    "T": "0101",

    "U": "0110",

    "V": "0111",

    "W": "1000",

    "X": "1001",

    "Y": "1010",

    "Z": "1011",

    ".": "1100",

    ",": "1101",

    ":": "1110",

    " ": "1111"

}
 
user_choice = input("Znak > Cesta / Cesta > Znak / Dekódování / Zakódování \n1/2/3/4: ")
 
 
################# ZNAK > CESTA

if user_choice == "1":

    user_input = input("Znak: ")

    print(tree[user_input])
 
################# CESTA > ZNAK

elif user_choice == "2":

    user_input = input("Cesta: ")

    for key, value in tree.items():

        if value == user_input:

            print(key)
 
################# DEKÓDOVÁNÍ

elif user_choice == "3":

    user_input = input("Dekódování: ")

    user_input = user_input.split("/")

    output = []

    for bin_seq in user_input:

        for key, value in tree.items():

            if value == bin_seq:

                output.append(key)

    print("".join(output))
 
################# ZAKÓDOVÁNÍ

elif user_choice == "4":

    user_input = input("Zakódování: ")

    output = []

    for char in user_input:

        output.append(tree[char])

    print("/".join(output))