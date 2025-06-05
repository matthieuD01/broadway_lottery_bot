from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

import undetected_chromedriver as uc

chrome_options = Options()
service = Service(
    "C:\\Users\\matth\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
driver = uc.Chrome(service=service, options=chrome_options)
driver.maximize_window()


def broadway_direct(driver, show: str, n_t: int = 2, popup=False):
    driver.switch_to.new_window(f'tab-{show}')
    url = f'https://lottery.broadwaydirect.com/show/{show}/'
    driver.get(url)
    wait = WebDriverWait(driver, 5)
    # print("Window opened!")
    if popup:
        try:
            accept_cookie_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.wpgdprc-button.wpgdprc-button--accept"))
            )
            accept_cookie_button.click()
            print("Cookie popup closed!")
        except:
            print("No cookie popup found (or took too long).")
    try:
        enter_button = driver.find_element(
            By.CSS_SELECTOR, "a.btn.btn-primary.enter-button.enter-lottery-link")
    except:
        try:
            closed_button = driver.find_element(
                By.CSS_SELECTOR, "a.btn.btn-default.closed-button.dlslot-disabled")
            # print('Lottery closed for', show)
        except:
            print(
                f'Error for show {show}: neither \'Enter lottery\' nor \'Closed\' button found.')
            return

    enter_button.click()
    # print('Button clicked...')
    iframe = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "iframe.fancybox-iframe"))
    )
    # print(f'Pop-up found! Switching to it...')

    driver.switch_to.frame(iframe)
    form_selector = "form.dlslot-entry-form"
    # print('Looking for form...')
    popup_form = driver.find_element(By.CSS_SELECTOR, form_selector)
    form_to_fill = {
        "dlslot_name_first": "Matthieu",
        "dlslot_name_last":  "Dominici",
        "dlslot_ticket_qty":  n_t,
        "dlslot_email":      "matthieu.dmnc@gmail.com",
        "dlslot_dob_month": "01",
        "dlslot_dob_day": "26",
        "dlslot_dob_year": "2000",
        "dlslot_zip": "10025",
        "dlslot_country": "2",
    }

    for field_name, value in form_to_fill.items():
        if field_name == "dlslot_country":
            country_dropdown = driver.find_element(
                By.CSS_SELECTOR, "select#dlslot_country")
            select = Select(country_dropdown)
            select.select_by_value(value)
        elif field_name == "dlslot_agree":
            agree_checkbox = driver.find_element(
                By.CSS_SELECTOR, "input#dlslot_agree")
            # driver.execute_script(
            #     "arguments[0].scrollIntoView(true);", agree_checkbox)
            driver.execute_script("arguments[0].click();", agree_checkbox)
            # agree_checkbox.click()
        else:
            field = popup_form.find_element(By.NAME, field_name)
            field.send_keys(value)

    WebDriverWait(driver, 60).until(EC.staleness_of(iframe))
    # print("Form sent and pop-up closed.")


shows_bway_direct = {
    'aladdin': 2,
    'dbh-nyc': 1,
    'mj-ny': 2,
    'st-nyc': 2,
    'six-ny': 2,
    'the-lion-king': 2,
    'wicked': 1,
}
shows = {
    'broadway_direct': shows_bway_direct
}

for platform, show_list in shows.items():
    print('Going through shows from', platform)
    if platform == 'broadway_direct':
        popup = True
        for show, n_t in show_list.items():
            print('Opening tab for', show)
            try:
                broadway_direct(driver, show, n_t=n_t, popup=popup)
            except Exception as e:
                print(f'Failed to get {show}, error: ', e)
            popup = False
            print('Completed form for', show)
        time.sleep(.5)

# broadway_direct(driver, 'the-lion-king', n_t = 2, popup=True)

driver.quit()
print('Session closed.')
