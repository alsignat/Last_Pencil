import random

NAMES = ("John", "Jack")


def generate_turn(pencils):
    if pencils == 1:
        return 1
    elif pencils % 4 == 1:
        return random.randint(1, 3)
    elif pencils % 4 == 0:
        return 3
    else:
        return pencils % 4 - 1


def input_pencils():
    pencils = input()
    if not pencils.isnumeric() or int(pencils) < 0:
        print("The number of pencils should be numeric")
        input_pencils()
    elif pencils == "0":
        print("The number of pencils should be positive")
        input_pencils()
    else:
        return int(pencils)


print("How many pencils would you like to use:")
pencils_elapsed = input_pencils()
first = input(f"Who will be the first ({NAMES[0]}, {NAMES[1]}):")
while first not in NAMES:
    first = input(f"Choose between {NAMES[0]} and {NAMES[1]}")
if first == NAMES[0]:
    second = NAMES[1]
else:
    second = NAMES[0]

player = first
while True:
    print("|" * pencils_elapsed)
    if pencils_elapsed == 0:
        print(f"{player} won!")
        break
    print(f"{player}'s turn:")
    if player == "John":
        turn = input()
        if not turn.isnumeric() or not 0 < int(turn) < 4:
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(turn) > pencils_elapsed:
            print("Too many pencils were taken")
            continue
    else:
        turn = generate_turn(pencils_elapsed)
        print(turn)
    pencils_elapsed -= int(turn)
    player = second if player is first else first






