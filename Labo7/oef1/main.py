class Student:
    def __init__(self, naam, studentnummer):
        self.naam = naam
        self.studentnummer = studentnummer
        self.punten = []

    def voeg_punt_toe(self, vak, punt):
        self.punten.append((vak, punt))

    def bereken_gemiddelde(self):
        if not self.punten:
            return 0

        return sum(punt for _, punt in self.punten) / len(self.punten)


def main():
    aymen = Student("aymen", "s00001")
    aymen.voeg_punt_toe("Python", 17)
    aymen.voeg_punt_toe("Databases", 2)
    aymen.voeg_punt_toe("Web Programming", 12)
    print(f"{aymen.naam}: {aymen.bereken_gemiddelde():.1f}")

    lennert = Student("lennert", "s00002")
    lennert.voeg_punt_toe("Python", 15)
    lennert.voeg_punt_toe("Databases", 11)
    lennert.voeg_punt_toe("Web Programming", 16)
    print(f"{lennert.naam}: {lennert.bereken_gemiddelde():.1f}")

    tristan = Student("tristan", "s00003")
    tristan.voeg_punt_toe("Python", 11)
    tristan.voeg_punt_toe("Databases", 5)
    tristan.voeg_punt_toe("Web Programming", 9)
    print(f"{tristan.naam}: {tristan.bereken_gemiddelde():.1f}")


if __name__ == "__main__":
    main()
