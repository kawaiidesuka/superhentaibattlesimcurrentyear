from random import randint

def statprint(self):
    print("tea: " + str(tea))
    print("clothing: " + str(clothing))
    print("fatigue: " + str(fatigue))
    print("head: " + str(head))
    print("torso: " + str(torso))
    print("left arm: " + str(larm))
    print("right arm: " + str(rarm))
    print("left leg: " + str(lleg))
    print("right leg: " + str(rleg))
    print("monster: " + str(monster))
    return

def limbhit(self):
    if limb == 0:
        head = head - damage
    elif limb == 1:
        torso = torso - damage
    elif limb == 2:
        larm = larm - damage
    elif limb == 3:
        rarm = rarm - damage
    elif limb == 4:
        lleg = lleg - damage
    elif limb == 5:
        rleg = rleg - damage
    return

tea = 100
clothing = 100
fatigue = 0
head = 100
torso = 100
larm = 100
rarm = 100
lleg = 100
rleg = 100
monster = 500

print("""
you hear slithering in the distance
you quickly change into a maid costume
you draw your water gun
you are ready to face the lurking cephalopod
""")

input("press enter to load your weapon with hot tea")

while monster > 0:
    dodge = randint(0,5)
    limb = randint(0,5)

    print("-----------------------------")
    input("press enter to use moe powers")
    print("-----------------------------")

    damage = randint(0,29)

    monster = monster - damage

    print("you spray hot tea on the tentacle monster for " + str(damage) + " damage")

    damage = randint(0,29)

    if limb == 0:
        head = head - damage
    elif limb == 1:
        torso = torso - damage
    elif limb == 2:
        larm = larm - damage
    elif limb == 3:
        rarm = rarm - damage
    elif limb == 4:
        lleg = lleg - damage
    elif limb == 5:
        rleg = rleg - damage
    print("the monster strikes back for " + str(damage) + " damage")

    reducestat = randint(0,9)
    fatigue = fatigue + reducestat

    reducestat = randint(0,9)
    tea = tea - reducestat

    reducestat = randint(0,9)
    clothing = clothing - reducestat

    statprint(0)
