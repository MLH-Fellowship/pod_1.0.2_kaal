#! /usr/bin/python3

import datetime
import json
import os
import pathlib
import subprocess
import time

import requests

# The ticker script creates a moropy.sh file in the tmp folder
# to keep the status of ticker. 0 - ticker should stop,
# 1 - ticker should keep running
# At each second the ticker will check the status from the file
# and then execute the command of getting the active window.

root_dir = pathlib.Path.home()
moropy_dir = os.path.join(root_dir, ".moropy")
status_file_name = "status"
credentials_file_name = "creds.json"
status_file_path = os.path.join(moropy_dir, status_file_name)
credentials_file_path = os.path.join(moropy_dir, credentials_file_name)
flush_file_path = "flush.csv"
base_url = "https://kaal-backend.herokuapp.com"


def read_user_data():

    with open(credentials_file_path, 'r') as file:

        json_object = json.load(file)
        return json_object


def write_to_file(filename, process, start_time):

    if len(process) == 0:
        return

    end_time = datetime.datetime.utcnow()
    duration = (end_time - start_time).total_seconds()

    with open(filename, "a") as window_logs:
        window_logs.write(
            "{},{},{},{}\n".format(previous_window, start_time, end_time, duration)
        )


def push_to_database():

    user_data = read_user_data()
    activities = []
    total_time = 0

    with open("logs.csv", "rb") as file:

        while True:

            line = file.readline()

            if not line:
                break

            process, startTime, endTime, duration = line.decode('UTF-8').split(',')

            total_time += int(float(duration))

            activities.append(
                {
                    "name": process,
                    "start_time": startTime,
                    "end_time": endTime,
                    "duration": int(float(duration)),
                }
            )

    payload = {
        "userHash": user_data['userHash'],
        "activities": activities,
        "codingTime": total_time,
    }

    payload_json = json.dumps(payload)

    # print(payload_json)

    requests.post("{}/storeactivity/".format(base_url), payload_json)

    # print(response.status_code)

    # with open(flush_file_path, "w") as f:
    # f.write(payload_json)

    with open("logs.csv", "w") as file:
        pass


# writes active status to moropy.sh
with open(status_file_path, 'w') as file:
    file.write("1")

ticker_continue = True

previous_window = ""
previos_start_time = datetime.datetime.utcnow()
previos_push_time = datetime.datetime.utcnow()

with open("logs.csv", "w") as window_logs:
    pass

while ticker_continue:

    # reads the status from moropy.sh
    with open(status_file_path, 'rb') as file:
        script = file.readlines()
        ticker_continue = bool(int(script[0].decode('UTF-8')))

    if not ticker_continue:
        write_to_file("logs.csv", previous_window, previos_start_time)
        push_to_database()
        break

    if (datetime.datetime.utcnow() - previos_push_time).total_seconds() >= 1 * 60:
        push_to_database()
        previos_push_time = datetime.datetime.utcnow()

    # if ticker_continue is false, ticker will stop after this iteration

    cmd = "xdotool getwindowfocus getwindowname getwindowpid"

    output = subprocess.getoutput(cmd)

    pid = output.split('\n')[1]

    process_name_cmd = "ps -p {} -o comm=".format(pid)

    process_name = subprocess.getoutput(process_name_cmd)

    if process_name != previous_window:

        with open("logs.csv", "a") as window_logs:

            write_to_file("logs.csv", previous_window, previos_start_time)

            previous_window = process_name
            previos_start_time = datetime.datetime.utcnow()

    time.sleep(0.5)
