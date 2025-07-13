def optimize_lamps(lamps_input):
    lamps = list(lamps_input)

    for i in range(1, len(lamps) - 1):
        if lamps[i - 1] == 'O' and lamps[i] == 'O' and lamps[i + 1] == 'O':
            lamps[i] = '-'

    return ''.join(lamps)

def main():
    lamps_input = input("Zadejte situaci v Hrochovníku: ")

    result = optimize_lamps(lamps_input)
    print("Optimalizovaná situace v Hrochovníku:")
    print(result)

if __name__ == "__main__":
    main()