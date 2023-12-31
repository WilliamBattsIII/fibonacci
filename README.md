# fibonacci
A quick project I put together in half an hour, where most of that half-hour was spent making it look nice...
...and then I went overboard with making it look nice and now it has all these features.

# Function
This program, aptly called `fibonacci`, computes Fibonacci numbers, starting with 0 and 1.  
It does basically what it says on the tin, adding the 2 numbers it has, putting that on top of the list, and then using the 2 most recent numbers to make the next number, in accordance with the Fibonacci sequence.

As a quick, quality-of-life feature, the program will print out how many Fibonacci numbers it's computed every 10,000 iterations.
This makes it easier if, for whatever reason, you want to stop only at a certain point (although the program can do that) -- or to track progress easily.

The first number of the Fibonacci sequence is 0. The second is 1. The third is also 1. The fourth is 2. The fifth is 3. The sixth is 5. The seventh is 8.
...and so on.

# Usage
Both of these programs do have log files, titled with `fib-{starttime}-log.txt`, where `{starttime}` is a Unix timestamp.
If you're using a set goal to calculate (see `--help argument`), you may choose to ignore or disable these as it prints out the desired Fibonacci number once it's finished computing it.
Additionally, the log files have a small note at the bottom, detailing the number of iterations calculated, the time the program ran for, and (in the form of Unix timestamps) the time it started/ended.

To stop execution, just press `^C`, and the program (should) exit cleanly.
Or crash it somehow, I don't care. (but it might mess up your log files)

There are several arguments used for setting limits of how far to compute, or to disable logging, and for various other uses -- run `fib.py --help` for help on them.
For a quick example, you can calculate up to the ten millionth Fibonacci number, without leaving any logs, printing notifications every 250K numbers by running the following:
`python3 fib.py -g 10000000 -i 250000 -n`

# Tips & Notes
- This program goes hard on the CPU, almost like a stress test, so be ready for that.
- Additionally, this program was written quickly in about half an hour, so there's no fancy algorithms to Get Stuff Done quicker, it's just pounding out addition after addition on a single core. As a weird coincidence, it turns out that how I happened to implement it was already quite fast.
- If it's doing something weird, please try to let it exit cleanly via `^C` first, since if you just force quit the whole thing, it could possibly corrupt the log files, and at the very least, you won't get the fancy Time Elapsed message at the end of the log file. Additionally, if you have the logging mode set to Efficient, you won't get a log file.
- If you know what coil whine is, and/or you get it on your computer, be ready for that, since it first confused me a bit since I didn't know what it ws. If you don't know what coil whine is, look it up -- it's quite interesting. (I use it to gauge how close the log file is to being done written to, since most of *my* coil whine comes from the NVMe drive)
- The log files are VERY LARGE, and I'd advise not opening the entire thing at once, as they can crash some text viewers. (cough, VS Code, cough) I recommend running `tail -n 5 fib-123ABC420-log.txt`, or something similar.
- Running without logs DRAMATICALLY increases the speed the program runs at, but unless you set a goal to go up to with `--goal`, it won't actually print out any Fibonacci numbers.
- For a rough idea of how long it takes to calculate up to a given point, you can run the program via the `time` command to measure how long it ran for.
- For anyone trying to squeeze the most performance they can out of this -- it's not RAM or GPU this uses. CPU is the main factor, while the program hardly uses any RAM. This program was tested on an 8th-gen Core i5, where calculating up to the 30 millionth number in the sequence took about an hour and a half. 100 million Fibonacci numbers would probably take around a day of nonstop running. 
- Have fun (?!)


If there are any issues or bugs or requests, please reach out to me! Consider leaving something in the Issues tab, or contributing with a pull request, on Github.

`coded with <3 in Python on a ThinkPad T490S`


William Batts III