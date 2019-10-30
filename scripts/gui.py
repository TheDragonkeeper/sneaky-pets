#!/usr/bin/python3
from consolemenu import *
from consolemenu.items import *
import curses, time, os, sys
sys.path.append('games')


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


def feed(pet):
	if pet["health"] <= pet["maxhealth"] and pet["hunger"] < pet["maxhunger"]:
		pet["currentemo"] = "excited"
		if pet["health"] > pet["maxhealth"]-10:
			pet["health"] = pet["maxhealth"]
		else:
			pet["health"] = pet["health"]+10
		if pet["hunger"] > pet["maxhunger"]-10:
			pet["hunger"] = pet["maxhunger"]
		else:
			pet["hunger"] = pet["hunger"]+10
	return pet

#def playsnake(pet):
#	import snake
#	snake.startsnake()

def menu(pet):
	menu = ConsoleMenu()
	feeditem = FunctionItem("Feed", feed(pet))
#	playitem = FunctionItem("Play Snake", playsnake(pet))
	# A CommandItem runs a console command
#	command_item = CommandItem("Run a console command",  "touch hello.txt")

	# A SelectionMenu constructs a menu from a list of strings
#	selection_menu = SelectionMenu(["item1", "item2", "item3"])

	# A SubmenuItem lets you add a menu (the selection_menu above, for example)
	# as a submenu of another menu
#	submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

	# Once we're done creating them, we just add the items to the menu
	menu.append_item(feeditem)
#	menu.append_item(playitem)
#	menu.append_item(command_item)
#	menu.append_item(submenu_item)

	# Finally, we call show to show the menu and allow the user to interact
	menu.show()
	return pet
