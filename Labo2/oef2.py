def bereken_taxi_prijs(afstand_km, is_weekend=False, is_nacht=False, is_luchthaven=False):
    BASIS_PRIJS=5
    PPK=2.5
    WEEKEND=3
    NACHT=5
    LUCHTHAVEN=7.5

    total = BASIS_PRIJS + (PPK*afstand_km)

    if is_weekend:
        total += WEEKEND
    
    if is_nacht:
        total += NACHT

    if is_luchthaven:
        total += LUCHTHAVEN

    return float(total)

def main():
    afstand = float(input("Afstand in kilometers: "))
    is_weekend = input("Is het weekend? (j/n): ") == "j"
    is_nacht = input("Is het nacht? (j/n): ") == "j"
    is_luchthaven = input("Is het een luchthaven-rit? (j/n): ") == "j"

    prijs = bereken_taxi_prijs(afstand_km=afstand,
                               is_weekend=is_weekend,
                               is_nacht=is_nacht,
                               is_luchthaven=is_luchthaven)
    print(f"Totaalprijs: €{prijs}")

if __name__ == "__main__":
    main()