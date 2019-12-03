import time
import click

#from os import system

#cls = lambda: system('cls')

def countdown(n):
    while n > 0:
        # Clear the screen
        click.clear()
        # print the number in the countdown
        print(n)
        # Pause the script for 1 second 
        time.sleep(1)
        # subtract 1 from the count
        n -= 1
        if n == 0:
            # Once n is 0, print a message or call a function
            click.clear()
            print('times up!')
            

if __name__ == "__main__":
    # If script is called directly, lets ask for some arguments - count
    import argparse
    parser = argparse.ArgumentParser(description="Simple Countdown app")
    parser.add_argument("count", type=int, help="Time to countdown")
    
    args = parser.parse_args()
    
    # Set a variable to our argument
    count = args.count
    
    # Call our function
    countdown(count)
