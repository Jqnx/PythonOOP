import math

straal = int(input("Geef de straal van de cilinder (in cm): "))
hoogte = int(input("Geef de hoogte van de cilinder (in cm): "))

volume = math.pi * (straal ** 2) * hoogte
print(f"Het volume van de cilinder is {round(volume, 1)} cm3")