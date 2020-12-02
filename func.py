import random

random_no = ['s', 'p', 'sc']
chance = 10
no_of_chance = 0
human_point = 0
comp_point = 0

print("stone paper and scissor game\n")
print("let's begin")

while no_of_chance < chance:
    inp = input("stone,paper,scissor")
    random = random.choice(random_no)

    if inp == random:
        print("Tie both 0 pt. to each other \n")

    elif inp == 's' and random == 'p':
        comp_point = comp_point + 1
        print(f"your guess is {inp} and computer choice is {random}")
        print("computer wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")

    elif inp == 'sc' and random == 'p':
        human_point = human_point + 1
        print(f"your guess is {inp} and computer choice is {random}")
        print("you wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")

    elif inp == 'p' and random == 'sc':
        comp_point = comp_point + 1
        print(f"your guess is {inp} and computer choice is {random}")
        print("computer wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")
    elif inp == 's' and random == 'sc':
        human_point = human_point + 1
        print(f"your guess is {inp} and computer choice is {random}")
        print("you wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")
    elif inp == 'sc' and random == 's':
        comp_point = comp_point + 1
        print(f"your guess is {inp} and computer choice is {random}")
        print("computer wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")

    elif inp == 'p' and random == 's':
        human_point = human_point + 1
        print(f"your guess is {inp} and computer choice is {random}")
        print("you wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")
    else:
        print("you entered wrong word")
        no_of_chance=no_of_chance+1
        print(f"{chance-no_of_chance} is left out of {chance}\n")

print('the game is over')
if comp_point>human_point:
    print("you loose the game")

else:
    print("hurray! you win the game")
print(f"your point is {human_point} and computer point is {comp_point}"
