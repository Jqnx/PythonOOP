import math

def main():
    zijde_a = int(input("Geef de lengte van zijde a: "))
    zijde_b = int(input("Geef de lengte van zijde b: "))

    zijde_c = bereken_hypotenusa(zijde_a, zijde_b)
    print(f"De hyptenusa heeft lengte: {zijde_c}")

def bereken_hypotenusa(zijde_a, zijde_b):
    return math.sqrt((zijde_a ** 2) + (zijde_b ** 2))

main()