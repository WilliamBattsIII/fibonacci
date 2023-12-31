# fibonacci
A quick project I put together in half an hour, where most of that half-hour was spent making it look nice

# Function
This program, aptly called `fibonacci`, computes Fibonacci numbers, starting with 0 and 1.  
It does basically what it says on the tin, adding the 2 numbers it has, putting that on top of the list, and then using the 2 most recent numbers to make the next number.

The first program, `fib.py`, just crunches numbers endlessly until you tell it to stop.

The second program, `fibcomputenth.py`, has a set goal in mind, and will stop at the Nth Fibonacci number, where N is set by changing the `fibIndexGoal` variable in code.

# Usage
Both of these programs do have log files, titled with either `fib-{starttime}-log.txt` or `FCnth-{starttime}-log.txt`.
If you're using `fibcomputenth.py`, you may choose to ignore these as it prints out the desired Fibonacci number once it's finished computing it.
As a quick note, the log files have a small note at the bottom, detailing the number of iterations calculated, the time the program ran for, and (in the form of Unix timestamps) the time it started/ended.

To stop execution, just press `^C`, and the program (should) exit cleanly.
Or crash it somehow, I don't care. (but it might mess up your log files)

# Tips & Notes
- This program goes hard on the CPU, almost like a stress test, so be ready for that.
- Additionally, this program was written quickly in about half an hour, so there's no fancy algorithms to Get Stuff Done quicker, it's just pounding out addition after addition on a single core.
- If it's doing something weird, please try to let it exit cleanly via `^C` first, since if you just force quit the whole thing, it could possibly corrupt the log files, and at the very least, you won't get the fancy Time Elapsed message at the end.
- If you know what coil whine is, and/or you get it on your computer, be ready for that, since it first confused me a bit since I didn't know what it ws. If you don't know what coil whine is, look it up -- it's quite interesting.
- The log files are VERY LARGE, and I recommend not opening the entire thing, as they can crash some text viewers. (cough, VS Code, cough) I recommend running `tail -n 5 fib-123ABC420-log.txt`, or something similar.
- Have fun (?!)

If there are any issues or bugs or requests, please reach out to me! Consider leaving something in the Issues tab, or contributing with a pull request, on Github.
`coded with <3 in Python on a ThinkPad T490S`