import time,os,sys

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
def emotionfiles(choice,emo):
	files = []
	giveemotion = []
	if emo == "normal":
		files = [ choice+"/"+choice+"1", choice+"/"+choice+"2", choice+"/"+choice+"3", ]
	if emo == "excited":
		files = [ choice+"/"+choice+"4" ]
	for emotionfile in files:
		with open(emotionfile,"r", encoding="utf8") as f:
			giveemotion.append(f.readlines())
	return giveemotion

def setuppet(choice):
	normal = emotionfiles(choice,"normal")
	excited = emotionfiles(choice,"excited")
	os.system('clear')
	print("You now have a pet "+choice+", Lets give it a name!")
	petname = input("What is your "+choice+"s name? :  ")
	os.system('clear')
	print("Lets meet your new "+choice+" "+petname+"....")
	time.sleep(5)
	os.system('clear')
	return petname,choice,normal,excited


def selected(pet, choice):
	pet["name"],pet["type"],pet["normal"],pet["excited"] = setuppet(choice)

def startsetup():
	os.system('clear')
	## menu make skip if not 1st run
	print("Welcome. Thank you for adopting your 1st Virtual Pet!")
	print("Choose an Animal:")
	print("1. Dog , q. quit")
	choice = input("Choice: ")
	options = {
		"1": selected(pet, "dog"),
		"q": sys.exit,
	}

	options[choice]

	return pet
