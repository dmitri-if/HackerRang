def minion_game(string):
    # your code goes here
    stuartScore, kevinScore = 0, 0
    for i in range(len(s)):
        if s[i] in ["A", "E", "I", "O", "U"]:
            kevinScore += len(s)-i
        else:
            stuartScore += len(s)-i
    if kevinScore > stuartScore:
        print("Kevin", kevinScore)
    elif kevinScore  < stuartScore:
        print("Stuart", stuartScore)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)