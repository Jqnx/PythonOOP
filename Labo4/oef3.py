def main():
    woorden = []
    gezien = set()
    while True:
        woord = input("Geef een woord (lege regel om te stoppen): ")
        if woord:
            woorden.append(woord)
        else:
            break

    print("Unieke woorden:")
    for woord in woorden:
        if woord not in gezien:
            gezien.add(woord)
            print(woord)


if __name__ == "__main__":
    main()
