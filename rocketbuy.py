import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import random

# 0.1 second ahead
BUY_TIME = "2019-11-05 19:59:59.90"
#BUY_TIME = "2019-11-05 16:56:59.90"
buy_time = datetime.strptime(BUY_TIME, '%Y-%m-%d %H:%M:%S.%f')
chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')

def login(driver, max_retries = 2):
    print("Try to login...")
    current_retry_login_times = 0
    login_success = False
    while current_retry_login_times < max_retries:
        current_retry_login_times += 1

        driver.get("https://www.tmall.com/")

        if driver.find_element_by_link_text("请登录"):
            time.sleep(5)
            driver.find_element_by_link_text("请登录").click()
            print("Scan QR Code to login")
            time.sleep(30)
            if driver.find_element_by_link_text('退出'):
                login_success = True
        else:
            print("Login Successfully...")
            login_success = True

        if login_success:
            break

    if not login_success:
        print("Failed to login")
        return False
    else:
        now = datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
        return True


def __refresh_keep_alive(driver,max):

    driver.get("https://cart.taobao.com/cart.htm")
    t = random.randint(1,max)
    t += 40
    print("Reload page before sleep {} sec".format(str(t)))
    time.sleep(t)

def keep_login_and_wait(driver):

    while True:
        currentTime = datetime.now()
        if (buy_time - currentTime).seconds > 60:
            __refresh_keep_alive(driver, 5)
        else:
            print("Close to buy time, stop reloading and wait")
            break

def buy(driver):
    #get the cart
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(random.randint(1,3))


    driver.find_element_by_id("J_SelectAll1").click()
    print("targets are selected in cart ")
    time.sleep(1.33)
    submit = driver.find_element_by_id("J_Go")

    # prepare submit button prepare
    button = EC.presence_of_element_located((By.CLASS_NAME, 'go-btn'))

    while True:
        time.sleep(0.01)
        if datetime.now() < buy_time:
            continue
        else:
            break

    start = datetime.now()
    submit.click()
    #driver.refresh()
    req_sent = datetime.now()
    try:
        # i find it takes more than 0.1 second to analysis a page, so poll_frequency is setting to 0.12
        #element = WebDriverWait(driver, timeout=3, poll_frequency=0.12).until(button)
        WebDriverWait(driver, timeout=3, poll_frequency=0.12).until(button)
        found = datetime.now()
        driver.execute_script("document.querySelector(\"[class='go-btn']\").click();")
        click = datetime.now()
    except TimeoutException:
        print("Loading took too much time!")


    print("Start: ", str(start))
    print("Sent : ", str(req_sent))
    print('Found: ', str(found))
    print('Click: ', str(click))


if __name__ == "__main__":

    if datetime.now() > buy_time:
        print("Error, check the bought time please")
        print("Exit...")
        exit(0)

    print("Opening Chrome browser...")
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    # option.add_argument('--disable-infobars')
    #disable - web - security allows chrome redirect and popup
    option.add_argument('disable-web-security')
    option.add_argument('silent')
    option.add_argument('log-level=0')

    driver = webdriver.Chrome(executable_path=chromedriver_path, options=option)

    driver.set_network_conditions(
        offline=False,
        latency=0,  # additional latency (ms)
        throughput=500 * 1024)  # maximal throughput

    print("chrome browser ready...")
    if login(driver, 1):
        keep_login_and_wait(driver)
        buy(driver)
