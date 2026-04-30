def main():
    positief = []
    nullen = []
    negatief = []

    while True:
        tekst = input("Geef een getal (lege regel om te stoppen): ")
        if not tekst:
            break
        else:
            num = int(tekst)
            if num == 0:
                nullen.append(num)
            elif num > 0:
                positief.append(num)
            else:
                negatief.append(num)

    print("Resultaat:")
    for num in negatief:
        print(num)

    for num in nullen:
        print(num)

    for num in positief:
        print(num)


if __name__ == "__main__":
    main()
