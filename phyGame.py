import sys

def getWord(inputWord,prompt):
    while len(inputWord) != 5:
        inputWord = input(prompt)
    return inputWord

def checkWord(i,mainWord,guessWord):
    if(mainWord[i]==guessWord[i]):
        print(mainWord[i],end="")
    else:
        for j in range(5):
            if mainWord[j]==guessWord[i]:
                print("*",end="")
                break
            if j==4:
                print("_",end="")

if __name__ == "__main__":
    mainWord = getWord(sys.argv[1],"please enter 5 char a WORD : ")
    for i in range(1,7):
        print(f"Lyf  : {7-i}")
        guessWord = getWord("","please input your 5 char guess WORD : ")
        for j in range(5):
            checkWord(j,mainWord,guessWord)
        print()
        if(mainWord == guessWord):
            print("You WON the game !")
            exit()
    print("You LOSE the game !")