def filter_extremen(lijst, n):
    if len(lijst) >= 2 * n + 1:
        gesorteerd = sorted(lijst)
        print(gesorteerd[n:-n])
    else:
        print("Fout: lijst bevat onvoldoende elementen")


def main():
    filter_extremen([1, 2, 3, 4, 5, 6, 7], 2)
    filter_extremen([10, 30, 20, 40, 60, 50, 80], 2)
    filter_extremen([-3, 3, -2, 2, -1, 1, 0], 1)


if __name__ == "__main__":
    main()
