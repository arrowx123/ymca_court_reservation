import sys
from selenium.webdriver.support.ui import Select
from ymca_court_reservation.utils import rest, rest_long, time_passed


def login(driver, login_id, account_pin):
    
    rest_long()
    rest_long()

    sign_in_button = driver.find_element_by_id('toolbar-login')
    sign_in_button.click()

    rest()

    login_id_input = driver.find_element_by_id("ClientBarcode")
    account_pin_input = driver.find_element_by_id("AccountPIN")

    login_id_input.send_keys(login_id)
    account_pin_input.send_keys(account_pin)

    sign_in_button_new = driver.find_element_by_id("Enter")
    sign_in_button_new.click()


def log_out(driver):
    rest_long()
    rest_long()
    logout_button = driver.find_element_by_id('toolbar-logout')
    logout_button.click()


def go_to_court_booking_page(driver):

    rest_long()
    court_reservation_button = driver.find_element_by_xpath(
        '//a[@href="../Facilities/FacilitiesSearchWizard.asp"]')
    court_reservation_button.click()


def find_booking_items(driver, start_day, start_month, end_day, end_month,
                       start_time, end_time, start_ampm, end_ampm):

    rest_long()
    facility_booking_radio = driver.find_element_by_id('search-facbook-radio')
    facility_booking_radio.click()

    badminton = '38'

    rest()
    start_day_dropdown = Select(driver.find_element_by_id('DayFrom'))
    start_month_dropdown = Select(driver.find_element_by_id('MonthFrom'))

    end_day_dropdown = Select(driver.find_element_by_id('DayTo'))
    end_month_dropdown = Select(driver.find_element_by_id('MonthTo'))

    start_time_dropdown = Select(driver.find_element_by_name('TimeFrom'))
    end_time_dropdown = Select(driver.find_element_by_name('TimeTo'))

    start_ampm_dropdown = Select(driver.find_element_by_name('AMPMFrom'))
    end_ampm_dropdown = Select(driver.find_element_by_name('AMPMTo'))

    funtion_dropdown = Select(driver.find_element_by_id('FacilityFunctions'))

    place_checkbox = driver.find_element_by_xpath('//*[@title="Guy-Favreau"]')

    start_day_dropdown.select_by_value(start_day)
    start_month_dropdown.select_by_value(start_month)

    end_day_dropdown.select_by_value(end_day)
    end_month_dropdown.select_by_value(end_month)

    start_time_dropdown.select_by_value(start_time)
    end_time_dropdown.select_by_value(end_time)

    start_ampm_dropdown.select_by_value(start_ampm)
    end_ampm_dropdown.select_by_value(end_ampm)

    funtion_dropdown.select_by_value(badminton)
    place_checkbox.click()

    while (True):
        search_button = driver.find_element_by_xpath('//*[@value="Search"]')
        search_button.click()
        rest_long()
        result_items = driver.find_elements_by_class_name('search-result-row')
        rest_long()

        if len(result_items) != 0 or time_passed():
            break

    select_cnt = 0
    if time_passed():
        sys.exit()

    for i in range(len(result_items)):
        id_ = 'chkBook' + str(i + 1)
        current_item = driver.find_element_by_id(id_)
        current_item.click()
        select_cnt += 1
        if select_cnt >= 2:
            break


def checkout(driver):

    add_button = driver.find_element_by_id('AddBookBottom')
    add_button.click()
    
    rest_long()
    rest_long()
    go_to_checkout_button = driver.find_element_by_xpath(
        '//*[@title="Click to Checkout"]')
    go_to_checkout_button.click()

    rest_long()
    rest_long()
    complete_transaction_button = driver.find_element_by_xpath(
        '//*[@title="Click to Complete Transaction"]')
    complete_transaction_button.click()
