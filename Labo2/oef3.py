def bereken_verzendkosten(aantal_artikelen, artikelprijs):
    totaal_bestelling = aantal_artikelen * artikelprijs
    
    eerste_artikel = 8.5
    volgende_artikels = (aantal_artikelen-1)*3

    if totaal_bestelling >= 50:
        return 0
    
    return float(eerste_artikel+volgende_artikels)

def main():
    artikel_prijs = int(input("Hoeveel kost je artikel? "))
    aantal_artikelen = int(input("Hoeveel heb je er gekocht? "))
    verzendkosten = bereken_verzendkosten(aantal_artikelen, artikel_prijs)

    print(f"Verzendkosten: €{verzendkosten}")

if __name__ == "__main__":
    main()