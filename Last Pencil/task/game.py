game_finished = False
names = ["John", "Jack"]

print("How many pencils would you like to use:")
while True:
    pencils = input()
    if not pencils.isnumeric() or int(pencils) < 0:
        print("The number of pencils should be numeric")
        continue
    elif pencils == "0":
        print("The number of pencils should be positive")
        continue
    else:
        pencils = int(pencils)
        break

first = input(f"Who will be the first ({names[0]}, {names[1]}):")
while first not in names:
    first = input(f"Choose between {names[0]} and {names[1]}")
if first == names[0]:
    second = names[1]
else:
    second = names[0]

player = first
while not game_finished:
    print("|" * pencils)
    while pencils > 0:
        print(f"{player}'s turn:")
        turn = input()
        if not turn.isnumeric() or not 0 < int(turn) < 4:
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(turn) > pencils:
            print("Too many pencils were taken")
            continue
        pencils -= int(turn)
        player = second if player is first else first
        if pencils > 0:
            print("|" * pencils)
        else:
            print(f"{player} won!")
            game_finished = True





