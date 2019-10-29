import time,os

def refresh(pet, emotion, question):
	for frame in pet[emotion]:
		print("Health: "+str(pet["health"])+"/"+str(pet["maxhealth"])+" "*10+str(pet["name"])+" "*10+"Hunger: "+str(pet["hunger"])+"/"+str(pet["maxhunger"])+"\n")
		print("".join(frame))
		if question == 0:
			print("\nM: Menu")
		else:
			print(str(question))
		time.sleep(1)
		os.system('clear')

def menuinput(userinput):
	question = 0
	if userinput == "m" or userinput == "M":
		question = "F: Feed  P: Play  S: Sleep"
	return question
