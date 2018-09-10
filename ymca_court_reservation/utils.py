from time import sleep
from datetime import datetime


def rest():
    sleep(0.1)


def rest_long():
    sleep(0.5)


def time_passed():
    now = datetime.now()
    #     print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    if now.minute >= 4 and now.minute <= 10:
        return True


def is_correct_time():
    now = datetime.now()
    #     print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    if (now.minute >= 58 and now.hour == 23) or now.hour == 0:
        return True
    return False


def read_secrets(secrets_dir):
    secrets = {}
    with open(secrets_dir, 'r') as f:
        for item in f.readlines():
            if item.startswith('#'):
                continue
            user, pass_ = item.split()
            secrets[user] = pass_
            print(user, pass_)
    return secrets
