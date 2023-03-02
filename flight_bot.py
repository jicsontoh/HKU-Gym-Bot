from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.common.by import By

ser = Service(r"/Applications/Google\ Chrome.app")
op = Options()
# op.add_argument('--headless')
driver = webdriver.Chrome(service=ser, options=op)


def flight_bot():
    print("Bot running...")

    try:
        # website to open
        driver.get("https://flights.cathaypacific.com/en_PH/offers/world-of-winners.html")
        sleep(30)

        # click on join now button

        # // img[@class ="imageWithFallback"]
        # link = driver.find_element(By.XPATH, "//a[normalize-space()='sign up now']")
        link = driver.find_element(By.XPATH, "//div[@id='Hong Kong Disneyland0.7957839503012754']")
        link.click()

        print("Success!")


    except Exception as e:
        print(e)
        return False

    finally:
        driver.quit()


if __name__ == "__main__":
    flight_bot()
