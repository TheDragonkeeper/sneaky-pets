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
	global question
	while True:
		time.sleep(20)
		userinputthread.terminate()
		userinputthread.start()
		question = 0

def userinput():
	global question
	while True:
		waitingoninput = input("")
		question = gui.menuinput(waitingoninput)
	
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
