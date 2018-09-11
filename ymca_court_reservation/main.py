from datetime import datetime
from selenium import webdriver

from ymca_court_reservation.base import login, log_out, go_to_court_booking_page, find_booking_items, checkout
from ymca_court_reservation.utils import read_secrets, is_correct_time, rest

if __name__ == "__main__":
    secrets_dir = './secrets.txt'
    secrets = read_secrets(secrets_dir)

    now = datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)

    # start_day = '8'
    start_day = str(now.day + 3)
    start_month = str(now.month)

    # end_day = '9'
    end_day = str(now.day + 3)
    end_month = str(now.month)

    start_time = '6'
    end_time = '10'

    # 0: am
    # 1: pm
    start_ampm = '1'
    end_ampm = '1'

    url = 'https://inscription.ymcaquebec.org'
    driver = webdriver.Chrome()
    driver.get(url)

    while (is_correct_time() is False):
        rest()

    for user in secrets.keys():
        login(driver, user, secrets[user])
        go_to_court_booking_page(driver)

        find_booking_items(driver, start_day, start_month, end_day, end_month,
                           start_time, end_time, start_ampm, end_ampm)

        checkout(driver)
        log_out(driver)
