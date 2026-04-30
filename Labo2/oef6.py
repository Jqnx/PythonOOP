def capitalize_sentences(tekst):
    new_tekst = ""
    chars = [" ", ".", "!", "?"]
    capitalize = False
    for letter in tekst:
        if letter != chars[0] and not capitalize:
            new_tekst += letter.upper()
            capitalize = True
        else:
            new_tekst += letter.lower()

        if letter in chars:
            capitalize = True

    return new_tekst

def main():
    tekst = " hallo wereld. hoe gaat het? geweldig! super."
    print(capitalize_sentences(tekst))

if __name__ == "__main__":
    main()