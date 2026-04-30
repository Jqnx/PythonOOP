def main():
    numbers = []
    while True:
        num = int(input("Geef een getal (0 om te stoppen): "))

        if num == 0:
            break
        else:
            numbers.append(num)

    print("Gesorteerde getallen:")
    for num in sorted(numbers):
        print(num)


if __name__ == "__main__":
    main()
