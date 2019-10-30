#!/usr/bin/python3
import os,sys,time
import os.path
sys.path.append('scripts')
import setup,gui
import threading
import json
from threading import Timer
os.system('clear')

pet = ""
menuactive = 0
if os.path.isfile("pet.json") == True:
	with open('pet.json', "r") as json_file:
		pet = json.load(json_file)
else:
	pet = setup.startsetup()
	with open("pet.json", "w") as write_file:
		json.dump(pet, write_file)


question = 0
def guiloop():
	global question
	while True:
		gui.refresh(pet,pet["currentemo"],question)
def resetinput():
	global pet
	global question
	while True:
		if pet["hunger"] > 0:
			pet["hunger"] = pet["hunger"]-1
		time.sleep(1)
		pet["currentemo"] = "normal"
#		userinputthread.terminate()
#		userinputthread.start()
		if pet["hunger"] == 0:
			pet["health"] = pet["health"]-1

		if pet["health"] <= 0:
			userinputthread.terminate()
			question = str(pet["name"]+" has Died")
			time.sleep(5)
			guithread.terminate()
			return

def userinput():
	global menuactive
	global question
	global pet
	while True:
#		waitingoninput = input("")
#		if waitingoninput == "m" or waitingoninput == "M":
#			menuitems = ['Feed', 'Play', 'Sleep', 'Exit']
		gui.menu(pet)
	
threads = []


guithread = threading.Thread(target=guiloop)
threads.append(guithread)

userinputthread = threading.Thread(target=userinput)
threads.append(userinput)

resetinputthread = threading.Thread(target=resetinput)
threads.append(resetinputthread)

guithread.start()
userinputthread.start()
resetinputthread.start()
