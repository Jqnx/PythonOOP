class BankRekening:
    def __init__(self, eigenaar, saldo=0.0):
        self.eigenaar = eigenaar
        self.saldo = saldo

    def stort(self, bedrag):
        if bedrag > 0:
            self.saldo += bedrag
            print(f"€{bedrag} gestort. Nieuw saldo: €{self.saldo}")

    def haal_af(self, bedrag):
        if bedrag <= self.saldo:
            self.saldo -= bedrag
            print(f"€{bedrag} afgehaald. Nieuw saldo: €{self.saldo}")
        else:
            print("Onvoldoende saldo")

    def toon_saldo(self):
        print(f"Saldo van {self.eigenaar}: €{self.saldo}")


def main():
    rekening = BankRekening("Jan", 100)
    rekening.stort(50.50)
    rekening.haal_af(30)
    rekening.haal_af(200)
    rekening.toon_saldo()


if __name__ == "__main__":
    main()
