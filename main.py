import os,sys,time
sys.path.append('scripts')
import setup,gui
os.system('clear')

pet = setup.startsetup()

while True:
	gui.refresh(pet,pet["currentemo"])
