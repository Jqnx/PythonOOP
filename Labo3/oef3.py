def bepaal_top5(scores):
    sorted_list = sorted(scores, reverse=True)
    return sorted_list[:5]

def bepaal_bottom5(scores):
    sorted_list = sorted(scores)
    return sorted_list[:5]

def main():
    scores = []
    print("Geef 10 scores:")
    for i in range(10):
        score = int(input(f"Score {i+1}: "))
        scores.append(score)

    print("\nTop 5 hoogste scores:")
    top5 = bepaal_top5(scores)
    for i,v in enumerate(top5):
        print(f"{i+1}. {v}")

    print("\nBottom 5 laagste scores:")
    bottom5 = bepaal_bottom5(scores)
    for i,v in enumerate(bottom5):
        print(f"{i+1}. {v}") 

if __name__ == "__main__":
    main()