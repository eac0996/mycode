#!/usr/bin/env python3

from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
swapper_score = 0
loaded_dice_score = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
    swapper.roll()
    loaded_dice.roll()

    swapper.cheat()
    loaded_dice.cheat()
    # Remove # before print statements to see simulation running
    # Simulation take ~1hr with prints and about 10s without

#print("Cheater 1 rolled" + str(swapper.get_dice()))
#print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
    #print("Draw!")
    elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
    #print("Dice Swapper wins!")
    swapper_score += 1
    else:
    #print("Loaded dice wins!")
    loaded_dice_score += 1


print("Simulation complete")
print("-------------------")
print("Final Scores")
print("------------")
print("Swaper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
if swapper_score == loaded_dice_score:
    print("Game was a draw")
    elif swapper_score > loaded_dice_score:
    print("Swapper wins!")
    else:
    print("Loaded dice wins!")

