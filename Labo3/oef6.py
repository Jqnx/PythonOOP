def merge_en_sorteer(lijst1, lijst2):
    new_list = lijst1[:]
    new_list.extend(lijst2)
    return sorted(new_list)

def main():
    lijst1 = [5, 2, 8]
    lijst2 = [3, 9, 1]
    print(merge_en_sorteer(lijst1, lijst2))

    print(lijst1)
    print(lijst2)

if __name__ == "__main__":
    main()