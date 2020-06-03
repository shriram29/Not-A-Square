from game import *
from misc_functions import *
from policy import *
from to_string import *


welcome ="""
\033[0;36m=================================================================\033[0m
\033[0;35m
██╗  ░█████╗░  ░██████╗░██████╗░██╗░░░██╗░█████╗░██████╗░███████╗
██║  ██╔══██╗  ██╔════╝██╔═══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝
██║  ███████║  ╚█████╗░██║██╗██║██║░░░██║███████║██████╔╝█████╗░░
╚═╝  ██╔══██║  ░╚═══██╗╚██████╔╝██║░░░██║██╔══██║██╔══██╗██╔══╝░░
██╗  ██║░░██║  ██████╔╝░╚═██╔═╝░╚██████╔╝██║░░██║██║░░██║███████╗
╚═╝  ╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝\033[0m
                                                        Alpha 1.0
\033[0;36mConcept By AB and Sai\033[0m

\033[1;32m< / > by Shriram\033[0m
\033[0;36m=================================================================\033[0m
"""
midgame="""
\033[0;36m=================================================================\033[0m \033[0;35m
██╗  ░█████╗░  ░██████╗░██████╗░██╗░░░██╗░█████╗░██████╗░███████╗
██║  ██╔══██╗  ██╔════╝██╔═══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝
██║  ███████║  ╚█████╗░██║██╗██║██║░░░██║███████║██████╔╝█████╗░░
╚═╝  ██╔══██║  ░╚═══██╗╚██████╔╝██║░░░██║██╔══██║██╔══██╗██╔══╝░░
██╗  ██║░░██║  ██████╔╝░╚═██╔═╝░╚██████╔╝██║░░██║██║░░██║███████╗
╚═╝  ╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝\033[0m
\033[0;36m=================================================================\033[0m
"""
clear()
print(welcome)
print("Please enter your name to continue: ",end="")
name=input()
clear()
print(midgame+"Welcome "+name+"!")
print("Enter Square Size: ",end="")
sqsize=int(input())
game = Game((sqsize, sqsize), ['X'])
loose=0
ende=int(sqsize*1.7)
print("Game will start with "+str(sqsize)+"x"+str(sqsize)+" square. You have "+str(ende)+" Turns.",end="")
printWait(4)
clear()

while loose==0 and ende>0:
    r=random.randint(1,5)
    movesArr=[]
    i=0
    while i<r+1:
        clear()
        print(midgame)
        print(game)
        print(str(ende)+" Turns left!")
        C='o '
        s='-----\n|'+C[r<1]+' '+C[r<3]+'|\n|'+C[r<5]
        print("\033[0;31m",end="")
        print (s+C[r&1]+s[::-1])
        print("\033[0m",end="")
        print("Die rolled "+str(r+1)+". You have "+str(r-i)+" more moves.")
        move=int(input("Enter move #"+str(i+1)+": "))
        try:
            game.select_edge(move, 'X')
            if game.get_score('X')>=1:
                break
        except Exception as e:
            print(e)
            print("Wait for 3 second.",end="")
            printWait(4)
            print()
            i=i-1
        finally:
            i=i+1
    if game.get_score('X')>=1:
        loose=1
    r=r-1
    print("Turn Completed. Rolling Die.",end="")
    printWait(3)
    ende=ende-1



if loose == 1:
    clear()
    print(game)
    print("\nYou lost :(")

if ende == 0:
    clear()
    print(game)
    print("\nYou Win :D")


print("\n\nGame Over.",end="")
printWait(15)