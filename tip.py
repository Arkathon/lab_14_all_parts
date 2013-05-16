"""
tip.py
=====
Create a tip calculator.

1. The program should ask the following:
    a. How many people?	
    b. How much did it cost?
    c. How was the service? 
        i.  The values for this can be: terrible, poor, ok, good, great
        ii. Only ask about service if there are less than 6 people
2. If the number of people are > 6 always tip should always be 20%, regardless of service.
3. Otherwise, calculate the tip using the following table:
    * terrible = no tip (0%)
    * poor - 10%
    * ok - 15%
    * good - 20%
    * great - 25%
4. Output the calculated tip.

Example Output (consider text after the ">" user input):

Run 1: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 2
How much did it cost? > 25
How was the service (terrible, poor, ok, good, great)? > great
You should probably tip $6.25!

 
Run 2: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 4
How much did it cost? > 70
How was the service (terrible, poor, ok, good, great)? > meh
Couldn't understand meh service; using default 15 percent.
You should probably tip $10.5!

Run 3: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 200
How much did it cost? > 950
You should probably tip $190.0!
"""

people = int(raw_input('How many people?\n>'))
cost = int(raw_input('How much did it cost?\n>'))
tips = [0.0, 0.1, 0.15, 0.20, 0.25]

if (people) in [1, 2, 3, 4, 5]:
    service = raw_input('How was the service?\n>')
    serv = ['bad', 'eh', 'ok', 'good', 'amazing']
    if service.lower() not in serv:

        print('I did not understand' + service + 'service; using the default 15%')
        tip = tips[2]
    else:
        tip = float(tips[serv.index(service)])
else:
    tip = tips[4]
print('You should consider tipping $' + str(cost*tip) + ' worth of cheese!')