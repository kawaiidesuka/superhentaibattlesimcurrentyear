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
print("you hear slithering in the distance")
print("you quickly change into a maid costume")
print("you draw your water gun")
print("you are ready to face the lurking cephalopod")
raw_input("press enter to load your weapon with hot tea")
while monster > 0:
	dodge = randint(0,5)
	limb = randint(0,5)
	print("--------------------")
	raw_input("press enter to use moe powers")
	print("--------------------")
	if clothing > 0 and fatigue < 100 and tea > 0:
		damage = randint(0,29)
		monster = monster - damage
		print("you spray hot tea on the tentacle monster for " + str(damage) + " damage")
		reducestat = randint(0,9)
		fatigue = fatigue + reducestat
		reducestat = randint(0,9)
		tea = tea - reducestat
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
		clothing = clothing - reducestat
		statprint(0)
	elif clothing <= 0 and fatigue < 100 and tea > 0:
		damage = randint(0,29)
		print("you spray hot tea on the tentacle monster for " + str(damage) + " damage")
		reducestat = randint(0,9)
		fatigue = fatigue + reducestat
		reducestat = randint(0,9)
		tea = tea - reducestat
		damage = randint(0,29) 
		if limb == 0:
			head = head - 10 - damage
		elif limb == 1:
			torso = torso - 10 - damage
		elif limb == 2:
			larm = larm - 10 - damage
		elif limb == 3:
			rarm = rarm - 10 - damage
		elif limb == 4:
			lleg = lleg - 10 - damage
		elif limb == 5:
			rleg = rleg - 10 - damage
		print("the monster strikes back for " + str(damage) + " damage")
		print("10 damage added due to nudity")
		statprint(0)
	elif clothing <= 0 and fatigue >= 100 and tea > 0:
		damage = randint(0,29)
		damage = damage - 5
		print("you spray hot tea on the tentacle monster for " + str(damage) + " damage")
		print("damage reduced by 5 due to fatigue")		
		reducestat = randint(0,9)
		fatigue = fatigue + reducestat
		reducestat = randint(0,9)
		tea = tea - reducestat
		damage = randint(0,29) 
		if limb == 0:
			head = head - 10 - damage
		elif limb == 1:
			torso = torso - 10 - damage
		elif limb == 2:
			larm = larm - 10 - damage
		elif limb == 3:
			rarm = rarm - 10 - damage
		elif limb == 4:
			lleg = lleg - 10 - damage
		elif limb == 5:
			rleg = rleg - 10 - damage
		print("the monster strikes back for " + str(damage) + " damage")
		print("10 damage added due to nudity")
		statprint(0)
	elif clothing <= 0 and fatigue >= 100 and tea <= 0:
		damage = randint(0,29)
		damage = damage - 10
		print("you spray hot tea on the tentacle monster for " + str(damage) + " damage")
		print("damage reduced by 10 due to fatigue and lack of tea")		
		reducestat = randint(0,9)
		fatigue = fatigue + reducestat
		reducestat = randint(0,9)
		tea = tea - reducestat
		damage = randint(0,29) 
		if limb == 0:
			head = head - 10 - damage
		elif limb == 1:
			torso = torso - 10 - damage
		elif limb == 2:
			larm = larm - 10 - damage
		elif limb == 3:
			rarm = rarm - 10 - damage
		elif limb == 4:
			lleg = lleg - 10 - damage
		elif limb == 5:
			rleg = rleg - 10 - damage
		print("the monster strikes back for " + str(damage) + " damage")
		print("10 damage added due to nudity")
		statprint(0)
	elif clothing > 0 and fatigue >= 100 and tea <= 0:
		damage = randint(0,29)
		damage = damage - 10
		print("you spray hot tea on the tentacle monster for " + str(damage) + " damage")
		print("damage reduced by 10 due to fatigue and lack of tea")		
		reducestat = randint(0,9)
		fatigue = fatigue + reducestat
		reducestat = randint(0,9)
		tea = tea - reducestat
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
		statprint(0)