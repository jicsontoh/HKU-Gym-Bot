import os
import re
import sys
import getopt
from telnetlib import EC
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

load_dotenv()

EMAIL = os.getenv("EMAIL")
NAME = os.getenv("NAME")
Student_no = os.getenv("STUDENT_NUM")

SER = Service("/Applications/Google\ Chrome.app")
LINK = "https://fcbooking.cse.hku.hk/Form/SignUp"

SESSIONS = {"CSE Active": {"1245-1415": "10123", "1715-1845": "10124"},
            "HKU B-Active": {"1700-1830": "10125", "1845-2015": "10126", "2030-2200": "10127"},
            "Stanley Ho Sports Centre": {"1745-1915": "10128", "1930-2100": "10129"}}

CENTRE = {"CSE": "CSE Active", "B-Active": "HKU B-Active", "SHSC": "Stanley Ho Sports Centre"}


def hku_gym_bot(centre_name, select_date, select_time):
    try:
        op = webdriver.ChromeOptions()
        # op.add_argument('--headless')
        # op.add_argument("start-maximized")
        op.add_argument("--incognito")
        op.add_argument("user-data-dir=selenium")
        op.add_experimental_option("excludeSwitches", ["enable-automation"])
        op.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(service=SER, options=op)

        print("Bot running...")
        # Open booking website
        driver.get(LINK)
        driver.set_window_size(893, 789)

        # Input email
        email = driver.find_element(By.XPATH, "//input[@id='Email']")
        email.send_keys(EMAIL)
        print("Keyed in Email")

        # Input name
        name = driver.find_element(By.XPATH, "//input[@id='FirstName']")
        name.send_keys(NAME)
        print("Keyed in Name")

        # Input Student no.
        student_no = driver.find_element(By.XPATH, "//input[@id='MemberID']")
        student_no.send_keys(Student_no)
        print("Keyed in Student No.")

        # Select gym centre
        centre = Select(driver.find_element(By.XPATH, "//select[@id='CenterID']"))
        centre.select_by_visible_text(centre_name)
        print(f"Selected Centre: {centre_name}")

        # Select Date
        date = Select(driver.find_element(By.XPATH, "//select[@id='DateList']"))
        # Date format: YYYY/MM/DD
        date.select_by_value(select_date)
        print(f"Selected Date: {select_date}")

        # Select timeslot
        time = Select(driver.find_element(By.XPATH, "//select[@id='SessionTime']"))
        time.select_by_value(select_time)
        print(f"Selected Time: {select_time}")

        # Click declaration
        data_collection = driver.find_element(By.XPATH, "//label[@for='dataCollection']")
        data_collection.click()
        print("Clicked declaration")

        # Bypass reCAPTCHA
        driver.execute_script("window.scrollTo(0, 988)")
        sleep(10)
        driver.implicitly_wait(10)
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

        print("Clicked Recaptcha")
        sleep(5)
        driver.switch_to.parent_frame()

        # Click submit
        select = driver.find_element(By.XPATH, "//button[@id='sbmtBtn']")
        select.click()
        print("Clicked Submit")

        sleep(30)
        print("Booking Success!")

    except Exception as e:
        print(f"[Bot error] {e}.")


def main(argv):
    try:
        centre = argv[0]
        date = argv[1]
        timeslot = argv[2]

        check_centre(centre)
        check_date(date)
        check_time(centre, timeslot)

        hku_gym_bot(CENTRE[centre], date, SESSIONS[CENTRE[centre]][timeslot])
    except Exception as e:
        print(f"[Input Error] {e}.")


def check_centre(centre):
    if centre not in CENTRE.keys():
        raise Exception("No such centre")


def check_date(date):
    # Input date format YYYY/MM/DD
    pattern = r'^\d{4}/\d{2}/\d{2}$'
    if not re.match(pattern, date):
        raise Exception("Wrong date format")


def check_time(centre, timeslot):
    if timeslot not in SESSIONS[CENTRE[centre]].keys():
        raise Exception("Timeslot not available in the selected centre")


if __name__ == "__main__":
    main(sys.argv[1:])
