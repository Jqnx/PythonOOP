def main():
    temps = []
    for i in range(7):
        temp = int(input(f"Temperatuur dag {i+1}: "))
        temps.append(temp)

    average = round(sum(temps) / len(temps), 1)
    above_average = 0

    for temp in temps:
        if temp > average:
            above_average = above_average+1

    print(f"Gemiddelde temperatuur: {average}°C")
    print(f"Hoogste: {max(temps)}°C")
    print(f"Laagste: {min(temps)}°C")
    print(f"Aantal dagen boven gemiddelde: {above_average}")


if __name__ == "__main__":
    main()