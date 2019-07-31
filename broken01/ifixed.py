#!/usr/bin/env python
calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != "q"):
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    operation = ""
        break
    calc1 = float(calc1)
    print("\What is the second operator? Or, enter q to quit: ")
    calc2 = input()
    if calc2 == "q":
        break
    calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -):  ")
    operation = raw_input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2"))
     if operation == '-':
            print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2"))
     else:
            print ("\n Not a valid entry. Restarting...")


 
