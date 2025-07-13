word = "radim"
guesses = []
tries = 10

done = False

while not done:
    for char in word:
        if char.lower() in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print("")
    
    guess = input(f"Počet pokusů {tries}, Další pokus: ")        
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        tries -= 1
        if tries == 0:
            break
        

    done = True
    for char in word:
        if char.lower() not in guesses:
            done = False
        
if done:
    print("Vyhrál jsi")
else:
    print("Prohrál jsi")
    

# .lower() = Mění velká písmena v textu na nalé.
    