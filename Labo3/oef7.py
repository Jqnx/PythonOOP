def vind_alle_indices(lijst, element):
    result = []

    for i, v in enumerate(lijst):
        if v == element:
            result.append(i)
    return result

def main():
    namen = ["Alice", "Bob", "Charlie", "Alice", "David", "Alice"]
    print(vind_alle_indices(namen, "Alice"))
    # [0, 3, 5]
    print(vind_alle_indices(namen, "Eve"))
    # []

if __name__ == "__main__":
    main()