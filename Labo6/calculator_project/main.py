from operations import add, subtract, multiply, divide


def main():
    while True:
        try:
            choice = int(input("""
Calculator
1. Optellen
2. Aftrekken
3. Vermenigvuldigen
4. Delen
0. Stoppen
"""))

            if choice == 0:
                break

            a = int(input("Geef eerste getal: "))
            b = int(input("Geef tweede getal: "))
        except ValueError:
            print("Geef een getal in.")

        else:
            match (int(choice)):
                case 1:
                    print(add(a, b))
                case 2:
                    print(subtract(a, b))
                case 3:
                    print(multiply(a, b))
                case 4:
                    try:
                        print(divide(a, b))
                    except ZeroDivisionError as e:
                        print(e)


if __name__ == "__main__":
    main()
