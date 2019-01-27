"""
Hangman.

Authors:  Hongyu Liu, Xinlai Chen, Zichen Tan
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.
import random
# Done: 2. Implement Hangman using your Iterative Enhancement Plan.
def main():
    while True:
        singele_game()
        game=str(input("Do you want a new game?(Y/N)"))
        if game=="N":
            break


def singele_game():
    print('Game has started.')
    string=get_random_string()
    print("The word has {} letters".format(len(string)))
    chance = 5
    rest=0
    l=[]
    for i in range(len(string)):
        l=l+["_ "]
    while True:
        count=0

        a=input('Write you guess here:')
        for k in range(len(string)):
            if a==string[k]:
                count+=1
                l[k]=a



        if count>0:
            print('Nice Guess')
            for i in range(len(l)):
                print(l[i],end="")

            print("")
            print("////////////////////////////")

        else:
            chance=chance-1
            print("Nanana")
            print("You have {} chance(s)".format(chance))
            print("////////////////////////////")
        if chance<1:
            print("You loss")
            break
        for i in range (len(l)):
            if l[k]=="_ ":
                rest=rest+1
        if rest==0:
            print("you win")
            print("The word is ' {} '".format(string))
            break
        rest=0



def get_random_string():
    with open('words.txt') as f:
        f.readline()
        string =f.read()
    words = string.split()
    x1 = len(words)

    r = random.randint(0,x1 - 1)
    item = words[r]

    return item
####### Do NOT attempt this assignment before class! #######

main()