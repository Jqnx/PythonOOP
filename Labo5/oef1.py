import sys


def main():
    try:
        file = sys.argv[1]
    except IndexError:
        print("Fout: Geef een bestandsnaam als argument")
    else:
        try:
            with open(file) as f:
                lines = f.readlines()[:10]
        except FileNotFoundError as e:
            print(f"Fout: Bestand '{e.filename}' niet gevonden")
        else:
            for line in lines:
                print(line.rstrip())


if __name__ == "__main__":
    main()
