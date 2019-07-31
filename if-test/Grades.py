#!/usr/bin/env python3
Score = input('Enter you test score: ')
if float(Score) >= 101:
    print('You enter an invalid number, please try again')
elif float(Score) >= 90:
    print("Congrats you got an A. Great job!!!")
elif float(Score) >= 80:
    print("Good Work you got a B")
elif float(Score) >= 70:
    print('Thats Ok you got a C')
elif float(Score) >= 60:
    print(' I can tell you really studied. You got a D')
else:
    print('You got an F which means failure')

