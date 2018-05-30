from Entity import Entity
from MessageQueue import Message, MessageQueue
import sys, os

clear = lambda: os.system('cls')
messageQueue = MessageQueue()

Player = Entity()
Opponent = Entity()

PlayerControl = 1
battling = True

while(Player.health > 0 and Opponent.health > 0 and battling == True):
    #Clear screen
    clear()

    #Print stats
    CharCount = len(Player.name+str(Player.health)+Opponent.name+str(Opponent.health))+7
    print('-' * CharCount)
    print("| %s:%d %s:%d |" % (Player.name, Player.health, Opponent.name, Opponent.health))
    print('-' * CharCount)

    if PlayerControl == 1:
        #attack or defend?
        command = input("Attack/Defend/Info/Exit/Restart: ")

        if command == "Attack":
            msg = Message(Opponent,Player,"damage",Player.attack)
            messageQueue.add(msg)
            PlayerControl = 0

        elif command == "Info":
            PMax = max(len(Player.name),len(str(Player.health))+3,len(str(Player.attack))+3)
            OMax = max(len(Opponent.name),len(str(Opponent.health))+3,len(str(Opponent.attack))+3)
            
            objList = Player.items()
            print(objList)

            print('-'*(PMax+OMax+7))
            print("| %s" % (Player.name), end='')
            print(" "*(PMax-len(Player.name)), end='')
            print(" | %s" % (Opponent.name), end='')
            print(" "*(OMax-len(Opponent.name)), end='')
            print(" |")
            print('-'*(PMax+OMax+7))

            print("| HP:%d" % (Player.health), end='')
            print(" "*(PMax-len(str(Player.health))-3), end='')
            print(" | HP:%d" % (Opponent.health), end='')
            print(" "*(OMax-len(str(Opponent.health))-3), end='')
            print(" |")

            print("| AT:%d" % (Player.attack), end='')
            print(" "*(PMax-len(str(Player.attack))-3), end='')
            print(" | AT:%d" % (Opponent.attack), end='')
            print(" "*(OMax-len(str(Opponent.attack))-3), end='')
            print(" |")
            print('-'*(PMax+OMax+7))
        
        elif command == "Exit":
            sys.exit(0)
        elif command == "Restart":
            battling = False
            break
        else:
            print("That command doesn't exist, please try again.\n")

        messageQueue.dispatch()

        input("Press Enter to continue...")

    else:
        msg = Message(Player,Opponent,"damage",Opponent.attack)
        messageQueue.add(msg)
        messageQueue.dispatch()
        PlayerControl = 1
        input("Press Enter to continue...")

if battling == False:
    print("Restarting game...")
    battling = True
elif Player.health <= 0:
    print("%s has died. Farewell brave soul." % (Player.name))
else:
	print("%s was slain. Huzzah!" % (Opponent.name))