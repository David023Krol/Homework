field = ["_" for i in range(5)]

input("hádej slovo  ")
word = "python"
for i in range(word):
    if i in word:
        print(i in len(word))
    else:
        print("písmeno není správné")

