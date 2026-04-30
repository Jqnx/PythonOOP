class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self.voorraad = voorraad

    def __str__(self):
        return f"{self.naam} - €{self.prijs} ({self.voorraad} stuks op voorraad)"


class Winkelmandje:
    def __init__(self):
        self.items = []

    def voeg_toe(self, product, aantal):
        if aantal <= product.voorraad:
            self.items.append((product, aantal))
        else:
            print("Onvoldoende voorraad")

    def bereken_totaal(self):
        totaal = 0
        for product, aantal in self.items:
            totaal += product.prijs * aantal
        return totaal

    def toon_inhoud(self):
        print("Winkelmandje:")
        for product, aantal in self.items:
            print(
                f"- {aantal}x {product.naam} - €{product.prijs} = €{product.prijs*aantal:.2f}"
            )


def main():
    laptop = Product("Laptop Dell XPS", 999.99, 5)
    muis = Product("Logitech MX Master", 89.99, 10)
    toetsenbord = Product("Keychron K2", 79.99, 3)

    mandje = Winkelmandje()

    mandje.voeg_toe(laptop, 1)
    mandje.voeg_toe(muis, 2)
    mandje.voeg_toe(toetsenbord, 10)

    mandje.toon_inhoud()
    print(f"\nTotaal: €{mandje.bereken_totaal():.2f}")


if __name__ == "__main__":
    main()
