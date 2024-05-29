# your code goes here!
import time
def countdown(b):
    while b > 0:
        print(f'{b} SECOND(S)!')
        b -= 1
    else:
        print("HAPPY NEW YEAR!")

        
def countdown_with_sleep(b):
    while b > 0:
        print(f'{b} SECOND(S)!')
        time.sleep(1)
        b -= 1
    else:
        print("HAPPY NEW YEAR!")

