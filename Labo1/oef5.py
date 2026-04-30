KLEIN = 0.12
GROOT = 0.25

kleine_flessen = int(input("Hoeveel kleine flessen lever je in? "))
grote_flessen = int(input("Hoeveel grote flessen lever je in? "))

ontvangst = (kleine_flessen * KLEIN) + (grote_flessen * GROOT)
print(f"Je ontvangt €{round(ontvangst, 2)} aan statiegeld.")