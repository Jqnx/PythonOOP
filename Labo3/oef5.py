def filter_even(getallen):
    return [i for i in getallen if i % 2 == 0]

def filter_positief(getallen):
    return [i for i in getallen if i > 0]

def filter_range(getallen, min_val, max_val):
    return [i for i in getallen if i in range(min_val, max_val+1)]

def main():
    getallen1 = [-5, -2, 0, 3, 7, 10, 15, 20]
    print(filter_even(getallen1))
    print(filter_positief(getallen1))
    print(filter_range(getallen1, 0, 10))

    getallen1 = []
    print(filter_even(getallen1))
    print(filter_positief(getallen1))
    print(filter_range(getallen1, 0, 10))

if __name__ == "__main__":
    main()