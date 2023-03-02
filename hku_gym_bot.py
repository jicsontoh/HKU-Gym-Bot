from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.common.by import By

ser = Service("/Applications/Google\ Chrome.app")
# ser = Service(r"/Applications/Google\ Chrome.app")

op = Options()
# op.add_argument('--headless')
driver = webdriver.Chrome(service=ser, options=op)

EMAIL = "u3611050@connect.hku.hk"
NAME = "Toh Ji Xiang Jicson"
Student_no = "3036110502"


def hku_gym_bot():
    print("Bot running...")

    try:
        # website to open
        driver.get("https://fcbooking.cse.hku.hk/Form/SignUp")
        driver.maximize_window()
        sleep(10)

        # click on join now button

        # // img[@class ="imageWithFallback"]
        # link = driver.find_element(By.XPATH, "//a[normalize-space()='sign up now']")
        # link = driver.find_element(By.XPATH, "//img[contains(@class,'largeHeader__logo')]")
        email = driver.find_element(By.XPATH, "//input[@id='Email']")
        email.send_keys(EMAIL)

        name = driver.find_element(By.XPATH, "//input[@id='FirstName']")
        name.send_keys(NAME)

        student_no = driver.find_element(By.XPATH, "//input[@id='MemberID']")
        student_no.send_keys(Student_no)

        sleep(30)

        print("Success!")


    except Exception as e:
        print(e)
        return False

    finally:
        driver.quit()


if __name__ == "__main__":
    hku_gym_bot()
