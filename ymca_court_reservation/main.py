import threading
from datetime import datetime
from selenium import webdriver

from ymca_court_reservation.base import (
    login, log_out, go_to_court_booking_page, find_booking_items,
    check_booking_items, checkout)
from ymca_court_reservation.utils import (read_secrets, is_correct_time, rest,
                                          passed_midnight)

if __name__ == "__main__":
    """
    to-do:
         1): 31 -> next month logic
         2): have a daily tmp file for recording used users
         3): run with CLI (flags: AM and PM)
     """

    secrets_dir = './secrets.txt'
    secrets = read_secrets(secrets_dir)

    now = datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    # start_day = '8'
    if passed_midnight():
        start_day = str(now.day + 2)
    else:
        start_day = str(now.day + 3)
    start_month = str(now.month)

    # end_day = '9'
    if passed_midnight():
        end_day = str(now.day + 2)
    else:
        end_day = str(now.day + 3)
    end_month = str(now.month)
    """
     test
     """
    # start_day = str(now.day + 1)
    # end_day = str(now.day + 1)

    start_time = '6'
    end_time = '12'

    # 0: am
    # 1: pm
    start_ampm = '1'
    end_ampm = '1'
    """
     test
     """
    # start_ampm = '0'
    # end_ampm = '0'

    while (is_correct_time() is False):
        rest()

    def book_court(user, secret):
        url = 'https://inscription.ymcaquebec.org'
        succ = False

        driver = webdriver.Chrome()
        driver.get(url)
        login(driver, user, secrets[user])

        while True:
            if is_correct_time() is False:
                break
            try:
                driver.get(url)
                go_to_court_booking_page(driver)

                find_booking_items(driver, start_day, start_month, end_day,
                                   end_month, start_time, end_time, start_ampm,
                                   end_ampm)
                check_booking_items(driver)

                checkout(driver)
                log_out(driver)
                succ = True
            except:
                pass
            if succ:
                break

        driver.close()

    for user in secrets.keys():
        threading.Thread(target=book_court, args=(user, secrets[user])).start()
