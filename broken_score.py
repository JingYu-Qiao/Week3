import random

def main():
    score = float(input("Enter score: "))
    rank = determine_Rank(score)
    print(rank)
    score=random.randint(0, 100)
    print(score)
    rank = determine_Rank(score)
    print(rank)

def determine_Rank(score):
    if score < 0:
        return ("Invalid score")
    elif score > 100:
        return ("Invalid score")
    elif score >= 50 and score < 90:
        return ("Passable")
    elif score >= 90:
        return ("Excellent")
    elif score < 50:
        return ("Bad")


main()