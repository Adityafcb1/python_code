import time
import random
a = [[1, 2, 3, 8, 9],
[7, 8, 13, 14, 15],
[4, 5, 6, 10, 11],
[11, 12, 16, 17, 18],
[3, 4, 9, 10, 15, 16],
[1, 2, 7, 8, 13, 14],
[5, 6, 11, 12, 17, 18]]

save = ["What a save by keeper", "Brilliant Save", "A Hero in the Making, What a Save", "The Wall, He Saves",
        "The unsung hero with the glove, He save it", "The best goalkeeper right now the world, Great Save",
        "Keeper guesses the right side and saves"]
score = ["Sends the keeper the wrong way", "There no way keeper was saving that", "Pure power, What a penalty",
         "Keeper guesses the right direction, but couldn't save it", "Calm as you like, He scores"]
miss = ["Hits the post and he misses", "Ohh no, he misses", "Hits the crossbar and a miss",
        "Sends the ball in the crowd what a miss that is"]

gf = 0
ga = 0
for i in range(1, 6):
    if i == 4 and (abs(gf - ga) == 3):
        break
    elif i == 5 and (abs(gf - ga) >= 2):
        break
    time.sleep(2)
    print("""
    Where would you like to shoot
    _____________________
    |*01*02*03*04*05*06*|
    |*07*08*09*10*11*12*|
    |*13*14*15*16*17*18*|
    """)
    n = int(input("I would like to shoot on: "))
    dive = random.choice(a)
    if n in range(1, 19):
        if n not in dive:
            time.sleep(2)
            print(random.choice(score))
            gf = gf + 1
            time.sleep(1)
            print("Score is: ", gf, "-", ga)
            print()
        else:
            time.sleep(2)
            print(random.choice(save))
            time.sleep(1)
            print("Score is: ", gf, "-", ga)
            print()
    else:
        time.sleep(2)
        print(random.choice(miss))
        time.sleep(1)
        print("Score is: ", gf, "-", ga)
        print()
    time.sleep(2)
    print("""
    Where you you like to Dive:
    ________________
    |*01* *04* *05*|
    |*02* *04* *06*|
    |*03* *04* *07*|
    """)
    m = int(input("Dive on: "))
    shoot = random.randint(0,21)
    if shoot in range(1, 18):
        if dive in range(1, 8):
            if shoot in a[m]:
                time.sleep(2)
                print(random.choice(save))
                time.sleep(1)
                print("Score is: ", gf, "-", ga)
                print()
            elif shoot not in a[m]:
                time.sleep(2)
                print(random.choice(score))
                ga = ga + 1
                time.sleep(1)
                print("Score is: ", gf, "-", ga)
                print()
        else:
            time.sleep(2)
            print(random.choice(score))
            ga = ga + 1
            time.sleep(1)
            print("Score is: ", gf, "-", ga)
            print()
    else:
        time.sleep(2)
        print(random.choice(miss))
        time.sleep(1)
        print("Score is: ", gf, "-", ga)
        print()
    print("Round", i, "Completed")

while gf == ga:
    print("We go to SUDDEN DEATH")
    time.sleep(2)
    print("""
        Where would you like to shoot
        _____________________
        |*01*02*03*04*05*06*|
        |*07*08*09*10*11*12*|
        |*13*14*15*16*17*18*|
        """)
    n = int(input("I would like to shoot on: "))
    dive = random.choice(a)
    if n in range(1, 19):
        if n not in dive:
            time.sleep(2)
            print(random.choice(score))
            gf = gf + 1
            time.sleep(1)
            print("Score is: ", gf, "-", ga)
            print()
        else:
            time.sleep(2)
            print(random.choice(save))
            time.sleep(1)
            print("Score is: ", gf, "-", ga)
            print()
    else:
        time.sleep(2)
        print(random.choice(miss))
        time.sleep(1)
        print("Score is: ", gf, "-", ga)
        print()
    time.sleep(2)
    print("""
        Where you you like to Dive:
        ________________
        |*01* *04* *05*|
        |*02* *04* *06*|
        |*03* *04* *07*|
        """)
    m = int(input("Dive on: "))
    shoot = random.randint(0, 21)
    if shoot in range(1, 18):
        if dive in range(1, 8):
            if shoot in a[m]:
                time.sleep(2)
                print(random.choice(save))
                time.sleep(1)
                print("Score is: ", gf, "-", ga)
                print()
            elif shoot not in a[m]:
                time.sleep(2)
                print(random.choice(score))
                ga = ga + 1
                time.sleep(1)
                print("Score is: ", gf, "-", ga)
                print()
        else:
            time.sleep(2)
            print(random.choice(score))
            ga = ga + 1
            time.sleep(1)
            print("Score is: ", gf, "-", ga)
            print()
    else:
        time.sleep(2)
        print(random.choice(miss))
        time.sleep(1)
        print("Score is: ", gf, "-", ga)
        print()

time.sleep(2)
print()
time.sleep(2)
print()
if gf > ga:
    print("You Won")
else:
    print("You Lost")
time.sleep(2)
print("Final Score: ", gf, "-", ga)
time.sleep(5)
print()


