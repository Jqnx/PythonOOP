dagen  = int(input("Aantal dagen: "))
uren  = int(input("Aantal uren: "))
minuten  = int(input("Aantal minuten: "))
seconden  = int(input("Aantal seconden: "))

seconden_in_dag = 60 * 60 * 24
seconden_in_uur = 60 * 60

dagen_in_seconden = dagen * seconden_in_dag
uren_in_seconden = uren * seconden_in_uur
minuten_in_seconden = minuten * 60

totaal = dagen_in_seconden + uren_in_seconden + minuten_in_seconden + seconden
print(f"Dit komt overeen met {totaal} seconden.")