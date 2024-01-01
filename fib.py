import time
import sys
import argparse

# fib.py
# WILLIAM BATTS III 2023

# The reason the below isn't in some sort of init() function is that I don't know if it'll mess with the (important) global scopes of all these things
starttime = str(int(time.time())) # our starting timestamp
sys.set_int_max_str_digits(0) # getting around a weird limitation with a weird hack
parser = argparse.ArgumentParser()

parser.add_argument('-n', '--nolog', default=False, help='Disables logging. Useful for stress tests and using goals (see below). (increases performance DRAMATICALLY)', action='store_true')
parser.add_argument('-g', '--goal', type=int, default=0, help='"goal" for how far to calculate (goal = the Nth fibonacci #) (GOAL must be a number) At the end of the calculation, it will print out the FULL number in the terminal (regardless of logging options)')
parser.add_argument('-i', '--index', type=int, default=10000, help='Print out Fibonacci sequence index every [i] iterations? Set as zero to disable these printouts. Default is 10K. (!!! recommended 5K+ !!!)')
parser.add_argument('-l', '--logging', type=str, default="onthefly", choices=["onthefly", "efficient", "o", "e"], help='Choose a logging style. Default is on-the-fly. On-the-fly logs while running. Efficient logs everything at the end, is faster, but may not save in a crash. (Note that Efficient will take an INCREDIBLY LONG TIME for anything higher than the 50,000th Fibonacci number.)')
parser.add_argument('-H', '--human', default=False, help='Show the index printouts in a human-readable format. (e.g., 1.8K, 250K, 15M, etc)', action='store_true')
args = parser.parse_args() # set up the arguments
fibIndexGoal = int(args.goal) # which fibonacci do we go to?
if(args.nolog == False): log = open(f"fib-{starttime}-log.txt", "w") # our log file
fibindex = args.index

if(args.logging == "onthefly" or args.logging == "o"):
    logstyle = 1
elif(args.logging == "efficient" or args.logging == "e"):
    logstyle = 0
else:
    print("Unknown logging style set! (this should be impossible)\n")


def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

def main():
    sequencelist = []
    a = -1 # Please disregard these variable names
    b = 1
    c = 0
    i = 0
    while True:
        try:
            c = a + b # math
            a = b
            b = c
            i = i + 1
            if(fibindex > 0):
                if(i % fibindex == 0 and fibindex != 0):
                   if(args.human == True):
                       print(human_format(i))
                   else:
                      print(i)

            if(logstyle == 1 and args.nolog == False):
                log.write(f"#{i}|| {c}\n\n")
            elif(logstyle == 0 and args.nolog == False):
                sequencelist.append(c)

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
    if(logstyle == 0 and args.nolog == False):
        print("\nlogging style set to 1 and logs are enabled -- generating log file (may take a while!)\n")
        for index, value in enumerate(sequencelist):
            try:
                log.write(f"#{index}|| {value}\n\n")
            except KeyboardInterrupt:
                print("\n!! exited during log file writing !!\n")
                exit()
    logtime = str(int(time.time()))
    if(args.human == True):
        iterations = human_format(int(i))
    else:
        iterations = int(i)
    if(args.nolog == False): log.write(f"\n\nEND AT {exittime} after {iterations} ITERATION(S). FOUND {int(i)}th FIB #. {int(exittime) - int(starttime)} SECONDS ELAPSED. (IF LOGGING STYLE SET TO EFFICIENT ->) TOOK {int(logtime) - int(exittime)}S TO LOG. START:{int(starttime)} // END:{int(logtime)}\n")

main()
if(args.nolog == False): log.close()
print("\nend")