import os,sys,time
sys.path.append('scripts')
import setup,gui
os.system('clear')

pet = {
	"name": None,
	"type": None,
	"normal": None,
	"excited": None,
	"health" : 100,
	"maxhealth": 100,
	"hunger" : 100,
	"maxhunger" : 100,
	"currentemo": "normal",
}

def selected(choice):
	global pet
	pet["name"],pet["type"],pet["normal"],pet["excited"] = setup.setuppet(choice)

os.system('clear')
## menu make skip if not 1st run
print("Welcome. Thank you for adopting your 1st Virtual Pet!")
print("Choose an Animal:")
print("1. Dog , q. quit")
choice = input("Choice: ")
options = {
	"1": selected("dog"),
	"q": sys.exit,
}

options[choice]

while True:
	gui.refresh(pet,pet["currentemo"])
