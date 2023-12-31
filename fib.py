import os
import time
import sys
import argparse

starttime = str(int(time.time())) # our starting timestamp
sys.set_int_max_str_digits(0) # getting around a weird limitation with a weird hack
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nolog', default=False, help='Disables logging. Useful for stress tests and avoiding large logs.', action='store_true')
parser.add_argument('-g', '--goal', type=int, default=0, help='"goal" for how far to calculate (goal = the Nth fibonacci #) (GOAL must be a number)')

args = parser.parse_args()
fibIndexGoal = int(args.goal) # which fibonacci do we go to?
if(args.nolog == False):
    log = open(f"FCnth-{starttime}-log.txt", "w") # our log file


def main():
    a = -1 # Please disregard my poor variable names, I might go back later and make the code look better
    b = 1
    c = 0
    i = 0
    while True:
        try:
            c = a + b # maff
            a = b
            b = c
            i = i + 1

            if(i % 10000 == 0): print(i)
            if(args.nolog == False): log.write(f"#{i}||   {c}\n\n") # Write to the log file, with the power of basic formatting and f-strings
            if(fibIndexGoal > 0):
                if(i == fibIndexGoal):
                    print(f"{fibIndexGoal}th FIBONACCI # IS {c}\n")
                    break
            elif(args.goal == 0):
                pass
            else:
                print("\nnegative fibonacci number goals not supported\n")
                if(args.nolog == False): log.write("\nnegative fibonacci number goals not supported\n")
                break
        except KeyboardInterrupt:
            break
        except SystemExit: # apparently except Exception doesn't catch this or KeyboardInterrupt, so here:
            break
        except Exception as e: # If it's not a ^C or SystemExit, then that's not good
            if(args.nolog == False): log.write(e) # log it
            print("\nsomething weird happened, check logs!")
            break

    exittime = str(int(time.time()))
    if(args.nolog == False): log.write(f"\n\nEXIT AT {exittime} after {int(i-1)} ITERATION(S). FOUND {int(i-1)}th FIB #. {int(exittime) - int(starttime)} SECONDS ELAPSED. START:{int(starttime)} // END:{int(exittime)}\n")

# please note that I tried vewwy hard to copy and paste the different comments across these files

main()
if(args.nolog == False): log.close()
print("\nend")