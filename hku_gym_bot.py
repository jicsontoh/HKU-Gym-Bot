from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ser = Service("/Applications/Google\ Chrome.app")
# ser = Service(r"/Applications/Google\ Chrome.app")

op = webdriver.ChromeOptions()
# op.add_argument('--headless')
# op.add_argument("start-maximized")
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=ser, options=op)

EMAIL = "u3611050@connect.hku.hk"
NAME = "Toh Ji Xiang Jicson"
Student_no = "3036110502"


def hku_gym_bot():
    print("Bot running...")

    try:
        # website to open
        driver.get("https://fcbooking.cse.hku.hk/Form/SignUp")
        # driver.maximize_window()
        driver.set_window_size(558, 430)

        # // img[@class ="imageWithFallback"]
        # link = driver.find_element(By.XPATH, "//a[normalize-space()='sign up now']")
        # link = driver.find_element(By.XPATH, "//img[contains(@class,'largeHeader__logo')]")
        email = driver.find_element(By.XPATH, "//input[@id='Email']")
        email.send_keys(EMAIL)

        name = driver.find_element(By.XPATH, "//input[@id='FirstName']")
        name.send_keys(NAME)

        student_no = driver.find_element(By.XPATH, "//input[@id='MemberID']")
        student_no.send_keys(Student_no)

        centre = Select(driver.find_element(By.XPATH, "//select[@id='CenterID']"))
        centre.select_by_visible_text("HKU B-Active")
        # centre.select_by_visible_text("CSE Active")

        date = Select(driver.find_element(By.XPATH, "//select[@id='DateList']"))
        date.select_by_value("2023/03/08")

        time = Select(driver.find_element(By.XPATH, "//select[@id='SessionTime']"))
        time.select_by_value("10125")

        data_collection = driver.find_element(By.XPATH, "//label[@for='dataCollection']")
        data_collection.click()

        # test = driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-border']")
        # WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
        #     (By.CSS_SELECTOR, "#recaptcha-anchor-label")))
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@class='recaptcha-checkbox-checkmark']"))).click()

        sleep(10)
        driver.implicitly_wait(10)
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()


        # submit = driver.find_element(By.XPATH, "//button[@id='sbmtBtn']")
        # submit.click()

        sleep(30)

        print("Success!")


    except Exception as e:
        print(e)
        return False

    finally:
        driver.quit()


if __name__ == "__main__":
    hku_gym_bot()
