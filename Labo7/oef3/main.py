class Bibliotheek:
    def __init__(self):
        self.boeken = []

    def voeg_boek_toe(self, boek):
        self.boeken.append(boek)

    def zoek_op_titel(self, titel):
        for boek in self.boeken:
            if titel.lower() == boek.titel.lower():
                return boek

        return None

    def toon_collectie(self):
        for boek in self.boeken:
            print(boek)


class Boek:
    def __init__(self, titel, auteur, isbn):
        self.titel = titel
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"{self.titel} door {self.auteur} (ISBN: {self.isbn})"


def main():
    bib = Bibliotheek()

    boek1 = Boek("Python Crash Course", "Eric Matthes", "978-1593279288")
    boek2 = Boek("Clean Code", "Robert Martin", "978-0132350884")
    boek3 = Boek("The Pragmatic Programmer", "Hunt & Thomas", "978-0135957059")

    bib.voeg_boek_toe(boek1)
    bib.voeg_boek_toe(boek2)
    bib.voeg_boek_toe(boek3)

    bib.toon_collectie()

    gevonden = bib.zoek_op_titel("clean code")
    if gevonden:
        print(f"\nGevonden: {gevonden}")


if __name__ == "__main__":
    main()
