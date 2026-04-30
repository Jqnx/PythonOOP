import random


def main():
    nummers = set()

    while len(nummers) < 6:
        nummers.add(random.randint(1, 49))

    gesorteerd = sorted(nummers)
    print("Jouw lotto nummers: " + ", ".join(str(v) for v in gesorteerd))


if __name__ == "__main__":
    main()
