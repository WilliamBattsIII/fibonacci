import os
import time
import sys

starttime = str(int(time.time())) # our starting timestamp
log = open(f"fib-{starttime}-log.txt", "w") # our log file
sys.set_int_max_str_digits(0) # getting around a weird limitation with a weird hack

def main():
    a = 0 # Please disregard my poor variable names, I might go back later and make the code look better
    b = 1
    c = 0
    i = -4 # i dunno lol
    while True:
        try:
            c = a + b # maff
            a = b
            b = c
            i = i + 1
            log.write(f"#{i}||   {c}\n\n") # Write to the log file, with the power of basic formatting and f-strings
        except KeyboardInterrupt:
            break
        except SystemExit: # apparently except Exception doesn't catch this or KeyboardInterrupt, so here:
            break
        except Exception as e: # If it's not a ^C or SystemExit, then that's not good
            log.write(e) # log it
            print("\nsomething weird happened, check logs!")
            break
    exittime = str(int(time.time()))
    log.write(f"\n\nEXIT AT {exittime} after {i} ITERATION(S). {int(exittime) - int(starttime)} SECONDS ELAPSED. START:{int(starttime)}//END:{int(exittime)}")

# please note that I tried vewwy hard to copy and paste the different comments across these files

main()
log.close()
print("\nend")