import random
random_no=['s','p','sc']
chance=10
no_of_chance=0
human_point=0
comp_point=0

print("\t\t\t snake,water and gun game\n\n")
print("let's begin")

while no_of_chance<chance:
    inp=input("snake,water ,gun")
    random=random.choice(random_no)

    if inp==random:
        print("Tie both 0 pt. to each other \n")

    elif inp=='s' and random=='p':
        comp_point=comp_point+1
        print(f"your guess is {inp} and computer choice is {random}")
        print("computer wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")

    elif inp=='sc' and random=='p':
        human_point=human_point+1
        print(f"your guess is {inp} and computer choice is {random}")
        print("you wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")

    elif inp=='p' and random==sc:
        comp_point=comp_point+1
        print(f"your guess is {inp} and computer choice is {random}")
        print("computer wins 1 points")
        print(f"computer points is {comp_point} and your point is {human_point}")