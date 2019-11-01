import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time
import random

BUY_TIME = "2019-11-01 20:00:00"
#BUY_TIME = "2019-11-01 16:15:00"
buy_time_object = datetime.datetime.strptime(BUY_TIME, '%Y-%m-%d %H:%M:%S')


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
    # 重新加载购物车页面，定时操作，防止长时间不操作退出登录
    driver.get("https://cart.taobao.com/cart.htm")
    t = random.randint(1,100)
    t += 60
    print("Reload page in case of timeout" + str(t) + "...")
    time.sleep(t)


def keep_login_and_wait(driver):
    #print("当前距离抢购时间点还有较长时间，开始定时刷新防止登录超时...")
    while True:
        currentTime = datetime.datetime.now()
        if (buy_time_object - currentTime).seconds > 180:
            __refresh_keep_alive(driver)
        else:
            print("Close to buy time, stop reloading and wait")
            break

def buy(driver):
    # 打开购物车
    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(1)

    submit_succ = False
    # 点击购物车里全选按钮
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
        print("targets selected in cart ")

    while True:
        time.sleep(0.01)
        if datetime.datetime.now() < buy_time_object:
            continue
        else:
            break
    try:
        # 点击结算按钮
        if driver.find_element_by_id("J_Go"):
            driver.find_element_by_id("J_Go").click()
            click_submit_times = 0
            while True:
                try:
                    if click_submit_times < 5:
                        driver.find_element_by_link_text('提交订单').click()
                        submit_succ = True
                        break
                    else:
                        if click_submit_times >= 5:
                            break
                        else:
                            print("Failed to submit...")
                except Exception as e:
                    print(e)
                    # print("没发现提交订单按钮，可能页面还没加载出来，重试...")
                    click_submit_times += 1
                    time.sleep(0.1)

                if submit_succ:
                    break

    except Exception as e:
        print(e)



if __name__ == "__main__":

    if datetime.datetime.now() > buy_time_object:
        print("Error, check the bought time please")
        print("Exit...")
        exit(0)

    print("Opening Chrome browser...")
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    # option.add_argument('--disable-infobars')
    #disable - web - security 可以允许浏览器重定向
    option.add_argument('disable-web-security')

    driver = webdriver.Chrome(executable_path=chromedriver_path, options=option)
    print("hrome browser ready...")
    if login(driver, 1):
        keep_login_and_wait(driver)
        buy(driver)
