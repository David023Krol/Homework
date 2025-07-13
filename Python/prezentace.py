def main():
    numbers = input("Zadejte čísla oddělená mezerou: ")
    numbers_list = [int(x) for x in numbers.split()]
    
    if len(numbers_list) == 0:
        print("Nebyla zadána žádná čísla.")
        return
    
    average = sum(numbers_list) / len(numbers_list)
    print("Průměr zadaných čísel je:", average)
    
    if average >= 50:
        print("Průměr je větší nebo roven 50.")
    else:
        print("Průměr je menší než 50.")

if __name__ == "__main__":
    main()

