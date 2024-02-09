#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO Add necessary rich.console and typer libraries.
# TODO: Use Console() to activate console printing 
# Add Your Name Here

def getAverage(start: int, end:int) -> float:
    """ function to determine average of input"""

    # declare variable before loop so
    # that it will exist after the loop has completed
    # and changed the variable.

    sum = 0
    
    for i in range(start, end):
        sum += i
    average = sum/(end - start) # calculate average
    # print(f" Average is :{average}")
    return average

# end of getAverage()

def is_prime(number: int) -> bool:
    """ Determine primality: return 0 and 1"""
    # Handle special cases for 0 and 1
    if number < 2:
        return False
    # Iterate from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        # If the number is divisible
        # by any value in the range, it's not prime
        if number % i == 0:
            return False
    # If no divisors are found, the number is prime
    return True
# end of is_prime()


# TODO: set cli to typer.Typer()

# TODO: add the decorator code: @cli.command()

# TODO: change the definition of main() to work with poetry
def main(start:int, end:int) -> None:
    """ driver program of program"""
    # print output to the user
    print(f"\n Starting value : {start}")
    print(f" Ending value : {end}\n")

    for i in range(start, end+1):
        print(f" {i} is prime: {is_prime(i)}")
    print(f"\n The average of the values between {start} and {end} is: {getAverage(start,end)}")

# end of main()    

# TODO for poetry to function using command line inputs, the below code will not be necessary.
        
# declare variables
start = 1
end = 10

# call the main function on execution
main(start, end) 
