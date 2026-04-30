def bereken_mediaan(a, b, c):
    return sorted([a,b,c])[1]

def main():
    a = int(input("Geef getal 1: "))
    b = int(input("Geef getal 2: "))
    c = int(input("Geef getal 3: "))

    mediaan = bereken_mediaan(a,b,c)
    print(f"De mediaan is: {mediaan}")

if __name__ == "__main__":
    main()