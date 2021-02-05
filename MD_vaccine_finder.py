"""

MD COVID Vaccine Appointment Finder
Matthew Tralka

for educational use only

"""

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


if os.name == "nt":
    import winsound

    def play_sound():
        winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        winsound.Beep(2500, 5000)


def highlight(element):

    driver = element._parent

    def apply_style(s):
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);", element, s
        )

    apply_style("background: yellow; border: 2px solid red;")


def main(URL, driver):
    global foundVaccine

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(URL)

    #####
    # LANDING
    #####

    elem = driver.find_element_by_xpath(
        "//button[@data-testid='landing-page-continue']"
    )
    elem.click()

    #####
    # SCREENING ELIGBLE
    #####

    elem = driver.find_element_by_xpath("//input[@name='q-screening-16-years-age']")
    elem.click()
    elem = driver.find_element_by_xpath("//input[@name='q-screening-healthdata']")
    elem.click()

    #####
    # RADIO ELIGBLE
    #####

    elems = driver.find_elements_by_xpath("//input[@name='q-screening-health-worker']")
    for option in elems:
        option_value = str(option.get_attribute("value")).upper()
        if option_value == "YES":
            option.click()

    elems = driver.find_elements_by_xpath(
        "//input[@name='q-screening-eligibility-age-range']"
    )
    for option in elems:
        option_value = str(option.get_attribute("value"))
        if option_value == AGE_RANGE:
            option.click()

    #####
    # CONT.
    #####

    elem = driver.find_element_by_xpath("//button[@data-testid='continue-button']")
    elem.click()

    #####
    # LOCATION
    #####

    elem = driver.find_element_by_xpath(
        "//input[@data-testid='location-search-address']"
    )
    elem.send_keys(ADDRESS)

    elem = driver.find_element_by_xpath(
        "//button[@data-testid='location-search-page-continue']"
    )
    elem.click()

    #####
    # AVAILABLE?
    #####

    NO_AVAIL = "'There are no locations nearby that have availability.'"

    try:
        elem2 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//p[contains(text(), {NO_AVAIL})]")
            )
        )

        if elem2:
            highlight(elem2)
            time.sleep(WAIT_TIME / 2)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        else:
            foundVaccine = True
            if os.name == "nt":
                play_sound()
    except:
        foundVaccine = True
        if os.name == "nt":
            play_sound()


if __name__ == "__main__":
    global driver
    global foundVaccine

    ##
    # ADJUST AS NEEDED
    ##

    # PATH to ChromeDrive
    # https://sites.google.com/a/chromium.org/chromedriver/downloads
    PATH = "./chromedriver.exe"
    WAIT_TIME: int = 5  # seconds
    ADDRESS: str = "3501 University Blvd E, College Park, MD, USA"
    AGE_RANGE: str = "16-49"
    # possible ranges
    # copy exactly as written
    # 16-49
    # 50-64
    # 65-74
    # 75 and Older

    URL = "https://massvax.maryland.gov/"
    foundVaccine = False

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(PATH, options=chrome_options)
    driver.implicitly_wait(2)
    driver.get("http://www.google.com")

    elem = driver.find_element_by_name("q")
    elem.send_keys(f"MD Vaccine Bot - searches every {WAIT_TIME + 5} seconds")
    time.sleep(2)

    while not foundVaccine:
        main(URL, driver)
        time.sleep(WAIT_TIME / 2)
    else:
        time.sleep(100000)
        driver.close()
