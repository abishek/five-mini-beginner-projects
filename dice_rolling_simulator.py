## Dice Rolling Simulator

# TODO: add argument support to change min-max limits

from random import Random

def roll_dice(random_simulator, choices) :

	return random_simulator.choice(choices)

def run_dice_rolling_simulator() :

	r = Random()
	choices = (1,2,3,4,5,6)
	print "Dice chose: ", roll_dice(r, choices)
	ui = None
	while not ui :
		ui = raw_input('Do you want to roll again? (y/n) ')
		if ui == 'y' :
			run_dice_rolling_simulator()
		elif ui == 'n':
			break
		else :
			ui = None


if __name__ == '__main__' :

	run_dice_rolling_simulator()

