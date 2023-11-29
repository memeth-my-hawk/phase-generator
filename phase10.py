import random

game = True

def phaseGenerator():

    actions = ["set", "run", "odd", "even", "color"]
    randAct = random.choice(actions)
    cards = random.randint(1, 9)

    if cards not in [3, 4] and randAct == "even" or randAct == "odd":
        print("Yalnız onu yapamıyoruz.")
    elif cards not in [2, 3, 4, 5] and randAct == "set":
        print("Yalnız onu yapamıyoruz.")
    elif cards not in [3, 4, 5, 6,] and randAct == "color":
        print("Yalnız onu yapamıyoruz.")
    elif cards not in [3, 4, 5, 6,] and randAct == "run":
        print("Yalnız onu yapamıyoruz.")
    else:
        print(randAct + " of " + str(cards))
   
    input("")
 
while game:
    #phases = int(input("how many phases? "))
    #phaseCounter = 1
    #while phaseCounter <= phases:
    #    phaseGenerator()
    #    phaseCounter += 1
    phaseGenerator()
   


