import os
import time
import sys

starttime = str(int(time.time())) # our starting timestamp
log = open(f"FCnth-{starttime}-log.txt", "w") # our log file
sys.set_int_max_str_digits(0) # getting around shit with a weird hack

fibIndexGoal = 100000 #which fibonacci do we go to?

def main():
    a = 1
    b = 2
    c = 0
    i = 0
    while True:
        try:
            c = a + b
            a = b
            b = c
            i = i + 1
            log.write(f"#{i}||   {c}\n\n")
        except KeyboardInterrupt:
            break
        if(i <= fibIndexGoal):
            print(f"{fibIndexGoal}th FIBONACCI # IS {c}\n")
            break
    exittime = str(int(time.time()))
    log.write(f"\n\nEXIT AT {exittime} after {i} ITERATION(S). {int(exittime) - int(starttime)} SECONDS ELAPSED.")

main()
log.close()
print("\nend")