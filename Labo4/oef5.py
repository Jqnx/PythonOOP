def formatteer_lijst(lijst):
    if not lijst:
        print("")
    elif len(lijst) == 1:
        print(lijst[0])
    elif len(lijst) == 2:
        print(f"{lijst[0]} en {lijst[1]}")
    elif len(lijst) >= 3:
        print(", ".join(lijst[:-1]) + " en " + lijst[-1])


def main():
    formatteer_lijst([])
    formatteer_lijst(["rozen"])
    formatteer_lijst(["rozen", "kranten"])
    formatteer_lijst(["rozen", "kranten", "ketels"])
    formatteer_lijst(["rozen", "kranten", "ketels", "wanten"])


if __name__ == "__main__":
    main()
