import sys


def main():
    try:
        file = sys.argv[1]
    except IndexError:
        print("Fout: Geef een bestandsnaam als argument")
    else:
        try:
            buffer = []
            with open(file) as f:
                for regel in f:
                    if len(buffer) == 10:
                        buffer.pop(0)
                        buffer.append(regel.rstrip())
                    else:
                        buffer.append(regel.rstrip())

        except FileNotFoundError as e:
            print(f"Fout: Bestand '{e.filename}' niet gevonden")
        else:
            for line in buffer:
                print(line)


if __name__ == "__main__":
    main()
