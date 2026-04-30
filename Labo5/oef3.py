import sys


def main():
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except FileNotFoundError as e:
                print(f"Fout: Bestand '{e.filename}' niet gevonden")
            else:
                for line in lines:
                    print(line.rstrip())
    else:
        print("Fout: Geen argumenten")


if __name__ == "__main__":
    main()
