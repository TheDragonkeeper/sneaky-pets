import time,os

def refresh(pet, emotion):
	for frame in pet[emotion]:
		print("Health: "+str(pet["health"])+"/"+str(pet["maxhealth"])+" "*10+str(pet["name"])+" "*10+"Hunger: "+str(pet["hunger"])+"/"+str(pet["maxhunger"])+"\n")
		print("".join(frame))
		time.sleep(1)
		os.system('clear')
