import urllib.request

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def checkout():

    add_button = driver.find_element_by_id('AddBookBottom')
    add_button.click()

    go_to_checkout_button = driver.find_element_by_xpath('//*[@title="Click to Checkout"]')
    go_to_checkout_button.click()

    complete_transaction_button = driver.find_element_by_xpath('//*[@title="Click to Complete Transaction"]')
    complete_transaction_button.click()

def log_out():
    sleep(0.1)
    logout_button = driver.find_element_by_id('toolbar-logout')
    logout_button.click()

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
