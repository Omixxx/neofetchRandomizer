import json
import sys
import subprocess
import random



file = open("/home/tut/Scripts/logos.json")
data = json.load(file)

def isClassicMode(mode : str) -> bool:
    if(mode == '1' or mode.casefold() == 'classic' ): return True
    return False


def isMinimalMode(mode :str)-> bool:
    if(mode == '2' or mode.casefold() == 'minimal' ):return True
    return False


def getRandomElementInAList(list):
    return list[random.randint(0,len(list)-1)] 

def getRandomClassicLogo() -> str:
    logos = []
    for logo in data['logos']:
            logos.append(logo)
    return getRandomElementInAList(logos)
    
def getRandomMinimalLogo()-> str:
    logos = []
    for logo in data['small_logos']:
        logos.append(logo)
    return getRandomElementInAList(logos) 
 
def main():
    if(isClassicMode(sys.argv[1])):
        command = getRandomClassicLogo()
        subprocess.run(["neofetch", "--ascii_distro", command])
    elif(isMinimalMode(sys.argv[1])):
        command = getRandomMinimalLogo() 
        subprocess.run(["neofetch", "--ascii_distro", command+"_small"])

        
if __name__ == "__main__":
    main()























