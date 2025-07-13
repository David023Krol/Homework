# # Zde se nachází seznam kódu který obsahuje poznámky z ročníku 1IT. Kapitoly jsou napsané TISKACÍM písmem.
# # Last updated 28/11/23


# # PROMĚNÉ A PODMÍNKY #

# # speed_ms = float(input("Zadej m/s: "))

# # speed_kmh = speed_ms * 3600 / 1000

# # print(speed_ms, "m/s je ", speed_kmh, "km/h")

# # temp_1 = 11
# # temp_2 = 21
# # temp_3 = 1

# # avg_temp = (temp_1 + temp_2 + temp_3*2) / 4




# # PROMĚNÉ #

# # a = 10
# # b = 15

# # if a > b:
#     # print("A je větší než B")
# # elif a < b: # I'd rather use else if on Lua than "elif" (⇀‸↼‶)💢
#      # print("B je větší než B")
# # else:
#     # print("A je rovno B")



# # Zadání #

# # a = input("Zadej velikost a ")
# # b = input("Zadej velikost b ")

# # if a == b:
#    # print("Čtverec má delku strany ",a,"cm")
# # else:
#    # print("Obdelník má délku strany ",a,"cm", b, "cm")


# # Zadání 2 #

# # x = 2
# # y = 4

# # if 4*x+3 < 5*y-1:
#    # print("Ano")
# # else:                 (ง •̀_•́)ง Python is annoying
#     # print("Ne")





# # POLE/SEZNAM #

# # List = [1, 2, 3, "Hello", 5] # Seznam (Pamatuj; List žačína 0, 1, 2, 3 atd.)

# # print(List[4]) # Vypiš Hello

# # List[1] = "Dva" # Přepiš list 1 (Číslo 2) na slovo "Dva"

# # List = [1, 2, 3, "Four", 5]

# # PŘIDÁVÁNÍ A ODEBRÁVÁNÍ ZE SEZNAMU #

# # List.append(6) # Na konec přidej číslo 6

# # List.pop(1) # Odeber ze seznamu 1 (číslo 2). Řada se poté mění. (Číslo 3 je jedna)
# # x = List.pop(0) # Odeber index ze seznamu (číslo 1). A dej ho do hodnoty x. Řada se poté mění (Číslo 3 je index)

# # List.remove("Four") # Odeber ze seznamu slovo "Four"




# # CYKLUS FOR #

# # List = [1, 2, 3] # Vytvoř seznam

# # for prvek in List: # Pro prvek v Listu
# 	# print(prvek) # Vypiš prvek (Vypíše celý seznam)

# # TextList = "Hello" # Vytvoř seznam

# # for character in TextList: # Pro charakter v TextListu
# 	# print(character) # Vypiš všechny hlásky

# # List = ["a", "b", "c"] # Vytvoř seznam

# # for i in range(len(List)): # Pro index v rangu (rozsah) "len" v listu  (Len bere všechny prvky)
# 	# print(List[i]) # Vypiš všechny hodnoty


# # Zadání #

# #Animals = [10, 5, 4]

# # x = Animals.pop(0)
# # y = Animals.pop(0)
# # z = Animals.pop(0)
# # c = x*2+y*4+y*4

# # print(c)import randomw, h, mines = 10, 5, 40# gene fieldfield = [[0 for y in range(h)] for x in range(w)]# put mine on random positionfor i in range(mines):    rx = random.randint(0, w - 1)    ry = random.randint(0, h - 1)    field[rx][ry] = "M"# print fieldfor y in range(h):    for x in range(w):        print(field[x][y], end="")    print()

# # # Možnost 2 #
# # # Animals = [10, 5, 4]

# # # Legs = Animals[0]*2 + Animals[1]*4 + Animals[2]*4

# # # print(Legs)


# # # Možnost 3 #
# # # Animals = [10, 5, 4]

# # # Legs = 0

# # # for i in range(len(Animals)):
# #    # for i == 0;
# #       # Legs += Animals[i]*2
# #    # else:
# #      # Legs += Animals[i]*4

# # # print(legs)
# # # (Funguje to tak že všechno vynásobí dvěmi a poté čtyřmi)



# # # Zadání 2 #

# # # Students_In_Class = [30, 28, 18, 19, 24]
# # # Number = 0
# # # for x in Students_In_Class:
# # #   Number += x
# # #   print(Number)

# # # Avg_Students = Number/len(Students_In_Class)

# # # print(Avg_Students)



# # # Zadání 3 #

# # # Numbers = [0,12,-3,2,-9,0,11]
# # # Hodnota_X = 0
# # # Hodnota_Y = 0
# # # Hodnota_Z = 0
# # # for x in Numbers:
# # #   if x > 0:
# # #      Hodnota_X += 1
# # #   elif x < 0:
# # #      Hodnota_Y += 1
# # #   else:
# # #      Hodnota_Z += 1



# # # FUNKCE #

# # # def function():
# #    # print("Hello World")

# # # function()

# # # Local script #
# # # def function():  Vytvoříme funkci pomocí "define"
# #    # Welcome = "Hello World" Vytvoříme proměnou se stringem
# #    # return Welcome "Vrátíme" proměnou
# # # print(function()) Vypíše funkci která obsahuje proměnou

# # # def multiply(number_1, number_2):
# #    # multiplied_number = number_1 * number_2
# #    # return multiplied_number

# # # print(multiply(10, 4))

# # def list_swap(list,old_num, new_num):
# #     for i in range(len(list)):
# #         if list[I] == old_num:
# #             list[i] = new_num
# #     return list

# # print(list_swap([2,5,8,6,2,4,7,2],2, 10))

# # def is_last_char_k(name):
# #     if name[len(name)] == "k":
# #         return True
# #     else:
# #         return False
    
# # print(is_last_char_k("Jakub"))

# # def card_hide(card_num):
# #     return 12*"*" + card_num[12:]

# # print(card_hide("1234567891014444"))

# # BMI Kalkulačka

# height = float(input("Zadej výšku v cm"))
# weight = float(input("Zadej váha v kg"))

# height/= 100

# bmi = weight/(height**2)

# if bmi <= 18.5:
#     return "Máš podváhu"
# elif bmi <= 24.9:
#     return"Jsi ok"


# OPAKOVÁNÍ
# proměné, list, datové typy

# var = 5 # integer +, -, *
# y = 16.0 # float
# text = "ahoj" # string +, *
# x = True # bool >, <, <=, ==, !=,... and, or, xor, nor
# arr = [1,8,"a",True] # list
# tup = (1,1,22,5) # tuple

# DVOJTÉ POLE
# Vysvětlení:
# Každý pole které je v [] má své číslo, abc je 1, def je 2.
# Mají své indexi, takže a je 0, b je 1 a c je 2. To samé platí pro [d,e,f].

# pole = [["a","b","c"],["d","e","f","g"]]
# print(pole[1][2])

#import random
#w, h, mines = 20, 5, 10
# gene field
#field = [[0 for y in range(h)] for x in range(w)]
 # put mine on random position
#for i in range(mines):
#    rx = random.randint(0, w - 1)
#    ry = random.randint(0, h - 1)
#    field[rx][ry] = "M"
#for y in range(h):
#    for x in range(w):
#        print(field[x][y], end="")
#    print()
#for y in range(h):
#    for x in range(w):
#        if field[x][y] == "M":
#            print("Mina na [{},{}]".format(x, y))

#arr = [["s","p","g","y"],
#       ["t","f","r","q"],
#       ["a","h","o","t"],
#       ["n","h","s","l"]]
#word = "python"
#current = 0

#for i in range(len(arr)):
#    for j in range(len(arr[i])):
#        if arr[i][j] == word[current]:
#            print(f"{word[current]} tam je na indexu [{i}[{j}]] ")
#            if current != len(word)-1:
#                current += 1
#if current == len(word)-1:
#    print(f"slovo{word} je v poli")
#else:
#    print(f"slovo {word} není v poli")

## dictionaries - slovníky

#person = {
#        "name": "Jakub",
#        "age": 22,
#        "pets": ["Nami", "Ten"]
#        }

#person["name"] = "Jakub Hájek"
#person["hair"] = "brown"

#for key in person.keys():
#    print(key)

#for values in person.values():
#    print(key)


