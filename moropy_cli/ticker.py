#! /usr/bin/python3

import os
import pathlib
import subprocess
import time

# The ticker script creates a moropy.sh file in the tmp folder
# to keep the status of ticker. 0 - ticker should stop,
# 1 - ticker should keep running
# At each second the ticker will check the status from the file
# and then execute the command of getting the active window.

root_dir = pathlib.Path.home()
moropy_dir = os.path.join(root_dir, ".moropy")
status_file_name = "status"
status_file_path = os.path.join(moropy_dir, status_file_name)


# writes active status to moropy.sh
with open(status_file_path, 'w') as file:
    file.write("1")

ticker_continue = True

file = open("info.txt", "w")

previous_window = ""

while ticker_continue:
    # reads the status from moropy.sh
    with open(status_file_path, 'rb') as file:
        script = file.readlines()
        ticker_continue = bool(int(script[0].decode('UTF-8')))

    if not ticker_continue:
        file.close()
        print("recieved close command, closing!")

    # if ticker_continue is false, ticker will stop after this iteration

    cmd = "xdotool getwindowfocus getwindowname"
    output = subprocess.getoutput(cmd)

    if output != previous_window:
        file.write(output)
        previous_window = output

    # sleeps for 0.5 second
    time.sleep(0.5)
