lengte = float(input("Geef je lengte in meter: "))
gewicht = float(input("Geef je gewicht in kilogram: "))

bmi = gewicht / (lengte**2)
print(f"Je BMI is {round(bmi, 1)}")

if bmi < 18.5:
    print("Dit valt in de categorie: ondergewicht")
elif bmi < 25:
    print("Dit valt in de categorie: normaal gewicht")
elif bmi < 30:
    print("Dit valt in de categorie: overgewicht")
else:
    print("Dit valt in de categorie: obesitas")