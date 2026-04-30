RENTE = 0.012

bedrag = int(input("Hoeveel stort je op je rekening? "))

for i in range(3):
    bedrag = bedrag + (bedrag * RENTE)
    print(f"Na {i+1} jaar: €{round(bedrag, 2)}")