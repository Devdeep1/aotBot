import random


def combat():
    combat_length = random.randrange(5, 10)
    print(f'you have {combat_length} moves')

    a = []
    moves = ['R', 'L']
    choices = []

    for i in range(0, combat_length):
        rand = random.choice(moves)
        a.append(rand)

        choice = input("what is your move (R/L) : ")

        if choice == a[i]:
            choices.append("T")
        else:
            choices.append("F")

        print(a)
        print(choices)

    def result(b):
        temp = ""
        length = len(b)
        for i in range(length):
            if b[i] == 'F':
                temp += "f"
            else:
                temp += "t"

        print(temp)

        f = 0
        t = 0
        for i in temp:
            if i == "f":
                f += 1
            else:
                t += 1

        if f > t:
            print("you died")
        else:
            print("you are alive")

    result(choices)


combat()