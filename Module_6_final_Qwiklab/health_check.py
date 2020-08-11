#! /usr/bin/env python3

import shutil
import psutil
import requests
import socket
import os, sys
import emails

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    if usage < 80:
        return True
    else:
        return False

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = 100* du.free / du.total
    # Min percent set to 20%
    min_percent = 20
    if free > min_percent:
        return True
    else:
        return False

def check_memory():
    mem = psutil.virtual_memory()
    # Memory treshold set to 500MB
    min_mem = 500 * 1024 * 1024
    if mem.available > min_mem:
        return True
    else:
        return False

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        return True
    else:
        return False

def send_email_data(subject_email):
    # Send email if there is an issue
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = subject_email
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

def main(argv):
    # TODO: DO all the checks
    if not check_cpu_usage():
        subject_email = "Error - CPU usage is over 80%"
        send_email_data(subject_email)
    elif not check_disk_usage("/"):
        subject_email = "Error - Available disk space is less than 20%"
        send_email_data(subject_email)
    elif not check_memory():
        subject_email = "Error - Available memory is less than 500MB"
        send_email_data(subject_email)
    elif not check_localhost():
        subject_email = "Error - localhost cannot be resolved to 127.0.01"
        send_email_data(subject_email)
    else:
        subject_email = "Everything is ok"
    print(subject_email)

if __name__ == "__main__":
  main(sys.argv)
