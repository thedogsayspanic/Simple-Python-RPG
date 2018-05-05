from Entity import Entity
import sys, os

clear = lambda: os.system('cls')

playerName = input("What is your name?: ")

Player = Entity(playerName)
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
            Player.attack_creature(Opponent)
            PlayerControl = 0
            
        elif command == "Defend":
            #set defense
            Player.defend()
            PlayerControl = 0

        elif command == "Info":
            CharCount = len(Player.name+Opponent.name)+7
            print('-' * CharCount)
            print("| %s | %s |" % (Player.name, Opponent.name))
            print("| HP:%d | HP:%d |" % (Player.health, Opponent.health))
            print("| AT:%d | AT:%d |" % (Player.attack, Opponent.attack))
            print("| DE:%d | DE:%d |" % (Player.defense, Opponent.defense))
            print("| DA:%s | DA:%s |" % (Player.defenseAdvantage, Opponent.defenseAdvantage))
            print('-' * CharCount)
        
        elif command == "Exit":
            sys.exit(0)
        elif command == "Restart":
            battling = False
            break
        else:
            print("That command doesn't exist, please try again.\n")
        
        input("Press Enter to continue...")
        #Clear screen
        clear()

    else:
        Opponent.attack_creature(Player)
        PlayerControl = 1
        input("Press Enter to continue...")
        #Clear screen
        clear()

if battling == False:
	print("Restarting game...")
elif Player.health <= 0:
    print("%s has died. Farewell brave soul." % (Player.name))
else:
	print("%s was slain. Huzzah!" % (Opponent.name))