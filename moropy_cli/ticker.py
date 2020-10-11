#! /usr/bin/python3

import datetime
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

previous_window = ""
previos_start_time = datetime.datetime.utcnow()

while ticker_continue:

    # reads the status from moropy.sh
    with open(status_file_path, 'rb') as file:
        script = file.readlines()
        ticker_continue = bool(int(script[0].decode('UTF-8')))

    if not ticker_continue:
        break

    # if ticker_continue is false, ticker will stop after this iteration

    cmd = "xdotool getwindowfocus getwindowname getwindowpid"

    output = subprocess.getoutput(cmd)

    pid = output.split('\n')[1]

    process_name_cmd = "ps -p {} -o comm=".format(pid)

    process_name = subprocess.getoutput(process_name_cmd)

    if process_name != previous_window and len(process_name) > 0:

        with open("logs.csv", "a") as window_logs:

            time_delta = (datetime.datetime.utcnow() - previos_start_time).total_seconds()

            window_logs.write("{},{}\n".format(previous_window, time_delta))

            previous_window = process_name
            previos_start_time = datetime.datetime.utcnow()

    time.sleep(0.5)
