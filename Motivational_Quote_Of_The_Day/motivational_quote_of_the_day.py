import datetime
import random


def getrandomquote():
    lines = open("../files/quotes.txt").read().splitlines()
    line = random.choice(lines)
    print()
    print("Motivational Quote of the Day")
    print(line)




if __name__ == '__main__':
    now = datetime.datetime.now()
    if now.strftime("%A") == "Monday":
        print("It's Monday! Time for some motivation!")
        getrandomquote()
    else:
        print("Today is",now.strftime("%A"))