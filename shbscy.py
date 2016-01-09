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

wound = 0
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
neko-chan hears slithering in the distance
neko-chan quickly changes into a maid costume
neko-chan draws her water gun
neko-chan is ready to face the lurking cephalopod
""")

input("press enter to load your weapon with hot tea")

while monster > 0:

    limb = randint(0,5)

    print("-----------------------------")
    input("press enter to use moe powers")
    print("-----------------------------")

    dialogue = randint(0,3)
    damage = randint(0,39)

    if head <= 0:
        damage -= 3
    if torso <= 0:
        damage -= 1
    if larm <= 0:
        damage -= 2
    if rarm <= 0:
        damage -= 2
    if lleg <= 0:
        damage -= 1
    if rleg <= 0:
        damage -= 1
    if fatigue >= 100:
        print("damage reduced by 5 due to fatigue")
        damage -= 5
    if tea <= 100:
        print("damage reduced by 5 due to lack of tea")
        damage -= 5

    if dialogue == 0:
        print("the tentacle monster screeches in agony")

    if dialogue == 1:
        print("neko-chan sticks her tongue out slightly, mocking the tentacle monster")

    if dialogue == 2:
        print("neko-chan teases the tentacle monster a bit"

    if dialogue == 3:
        print("neko-chan says 'nyaa~'")

    monster -= damage

    print("neko-chan sprays hot tea on the tentacle monster for " + str(damage) + " damage")

    damage = randint(0,39)

    if clothing <= 0:
        print("10 damage added for nudity")
        damage += 10

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

    reducestat = randint(0,3)
    fatigue += reducestat

    reducestat = randint(0,3)
    tea -= reducestat

    reducestat = randint(0,3)
    clothing = clothing - reducestat

    statprint(0)

print("it is not known whether or not the schoolgirl that ventured into that cave won her fight")
print("all we know is that japanese schoolgirls must never set foot there")
print("or much tentacle rape will occur")
print("a kawaiidesuka game")
