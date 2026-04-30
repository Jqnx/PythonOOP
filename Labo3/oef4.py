def verwijder_duplicaten(lijst):
    new_list = []
    seen = set()

    for i in lijst:
        if i not in seen:
            new_list.append(i)
            seen.add(i)

    return new_list

def main():
    list1 = verwijder_duplicaten([1, 2, 2, 3, 4, 3, 5])
    print(list1)

    list2 = verwijder_duplicaten(["appel", "peer", "appel", "banaan"])
    print(list2)

if __name__ == "__main__":
    main()