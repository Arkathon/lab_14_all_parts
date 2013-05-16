"""
name_that_roll.py
=====
Write a program that names the rolls of two dice in a dice game called craps...

* ask the user for the values of two dice rolls.  
* output the name of the roll using Wikipedia's article on Craps
	* http://en.wikipedia.org/wiki/Craps#Rolling
* only check for the following rolls:
	* _Snake Eyes_
	* _Hard Four_ 
	* _Easy Four_  
* print out "I don't know yet" for any other rolls.  Example output:
* example interaction:

What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 1
Snake Eyes!

Press ENTER or type command to continue
What roll did you get for the first die?
> 1
What roll did you get for the second die?
> 3
Easy Four
"""
roll1 = int(raw_input('What roll did you get for the first die?\n>'))
roll2 = int(raw_input('What roll did you get for the second die?\n>'))

if roll1 == 1 and roll2 == 1:
	print('Snake Eyes')
elif roll1 == 2 and roll2 == 2:
	print('Hard Four')
elif (roll1, roll2) in [(1, 3),(3, 1)]:
	print('Easy Four')
else:
	print('WAT. WHAT TYPE OF GAME ARE YOU PLAYING!')