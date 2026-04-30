def centreer_tekst(tekst, breedte):
    if len(tekst) >= breedte:
        return f"|{tekst}|"
    else:
        spaces = " " * ((breedte - len(tekst)) // 2)
        return f"|{spaces}{tekst}{spaces}|"
    
def main():
    print(centreer_tekst("Python", 25))
    print(centreer_tekst("Programmeren", 20))
    print(centreer_tekst("Hallo", 5))

if __name__ == "__main__":
    main()