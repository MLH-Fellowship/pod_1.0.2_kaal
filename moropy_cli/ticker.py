#! /usr/bin/python3

import time
import subprocess

# The ticker script creates a moropy.sh file in the tmp folder
# to keep the status of ticker. 0 - ticker should stop,
# 1 - ticker should keep running
# At each second the ticker will check the status from the file
# and then execute the command of getting the active window.


# writes active status to moropy.sh
with open('/tmp/moropy.sh', 'w') as file:
    file.write("1")

ticker_continue = True

while ticker_continue:
    # reads the status from moropy.sh
    with open('/tmp/moropy.sh', 'rb') as file:
        script = file.readlines()
        ticker_continue = bool(int(script[0].decode('UTF-8')))

    # if ticker_continue is false, ticker will stop after this iteration

    cmd = "xdotool getwindowfocus getwindowname"
    output = subprocess.getoutput(cmd)
    print(output)

    # sleeps for 0.5 second
    time.sleep(0.5)
