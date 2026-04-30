def add_item(groceries):
    item = input("Item: ")
    groceries.append(item)
    print(f"'{item}' toegevoegd.")

def remove_item(groceries):
    item = input("Item om te verwijderen: ")
    if item in groceries:
        groceries.remove(item)
        print(f"'{item}' verwijderd.")

def show_list(groceries):
    print("Boodschappenlijst:")
    for index, value in enumerate(groceries):
        print(f"{index+1}. {value}")

def clear_list(groceries):
    groceries.clear()
    print("Boodschappenlijst leeggemaakt.")

def main():
    print("""
=== Boodschappenlijst ===
1. Item toevoegen
2. Item verwijderen
3. Lijst tonen
4. Lijst wissen
5. Afsluiten
""")
    
    groceries = []


    while (True):
        choice = int(input("\nKeuze: "))

        match choice:
            case 1:
                add_item(groceries)
            case 2:
                remove_item(groceries)
            case 3:
                show_list(groceries)
            case 4:
                clear_list(groceries)
            case 5:
                print("Programma afgesloten.")
                break
            case _:
                print("Keuze niet beschikbaar, kies een nummer uit het menu.")

if __name__ == "__main__":
    main()