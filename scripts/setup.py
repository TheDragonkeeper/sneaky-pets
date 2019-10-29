import time,os
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

