import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import random

#BUY_TIME = "2019-11-04 19:59:59.95"
BUY_TIME = "2019-11-04 14:59:59.95"
buy_time = datetime.strftime(BUY_TIME, '%Y-%m-%d %H:%M:%S.ff')
chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')

def login(driver, max_retries = 2):
    print("Try to login...")
    current_retry_login_times = 0
    login_success = False
    while current_retry_login_times < max_retries:
        current_retry_login_times += 1

        driver.get("https://www.tmall.com/")

        if driver.find_element_by_link_text("请登录"):
            #print("没登录，开始点击登录按钮...")
            time.sleep(5)
            driver.find_element_by_link_text("请登录").click()
            print("Scan QR Code to login")
            time.sleep(20)
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
        now = datetime.datetime.now()
        print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
        return True


def __refresh_keep_alive(driver):

    driver.get("https://cart.taobao.com/cart.htm")
    t = random.randint(1,90)
    t += 60
    print("Reload page before sleep {} sec".format(str(t)))
    time.sleep(t)


def keep_login_and_wait(driver):

    while True:
        currentTime = datetime.datetime.now()
        if (buy_time - currentTime).seconds > 180:
            __refresh_keep_alive(driver)
        else:
            print("Close to buy time, stop reloading and wait")
            break

def buy(driver):
    #get the cart
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(1 + random.randint(2,5))
    time.sleep(0.33)

    driver.find_element_by_id("J_SelectAll1").click()
    print("targets are selected in cart ")

    while True:
        time.sleep(0.01)
        if datetime.now() < buy_time:
            continue
        else:
            break

    start = datetime.now()
    driver.find_element_by_id("J_Go").click()
    req_sent = datetime.now()
    try:
        element = WebDriverWait(driver, timeout=3, poll_frequency=0.01).until(EC.presence_of_element_located((By.LINK_TEXT, '提交订单')))
        element.click()
    except TimeoutException:
        print("Loading took too much time!")
    finally:
        end = datetime.now()

    print("Start: ", str(start))
    print("Sent : ", str(req_sent))
    print("End  : ", str(end))

if __name__ == "__main__":

    if datetime.datetime.now() > buy_time:
        print("Error, check the bought time please")
        print("Exit...")
        exit(0)

    print("Opening Chrome browser...")
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    # option.add_argument('--disable-infobars')
    #disable - web - security allows chrome redirect and popup
    option.add_argument('disable-web-security')

    driver = webdriver.Chrome(executable_path=chromedriver_path, options=option)
    print("hrome browser ready...")
    if login(driver, 1):
        keep_login_and_wait(driver)
        buy(driver)
