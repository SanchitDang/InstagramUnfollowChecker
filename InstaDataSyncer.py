import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Functions
def get_acc_you_follow():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(
        executable_path=r'DevChrome Data\chromedriver.exe',
        options=options)

    acc_you_follow = 'https://www.instagram.com/accounts/access_tool/accounts_you_follow'
    driver.get(acc_you_follow)

    acc_you_follow = open(r'Synced Data/acc_you_follow.txt', 'w')

    # Clicking button loop
    while True:
        try:
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='sqdOP  L3NKy   y3zKF     ']"))).click()
        except:
            break

    # Getting name loop
    xpath = "//div[@class='-utLf']"
    idx = 1  # here first class's index is 1 not 0, cuz its positioning not index
    while True:
        try:
            xpath_new = xpath + "[" + str(idx) + "]"
            user_id = driver.find_element_by_xpath(xpath_new).get_attribute('innerHTML')
            idx += 1
            acc_you_follow.write(user_id + '\n')

            """
            # Get Profile Pic
            try:
                # Class if u not following
                user_id_url = 'https://www.instagram.com/' + user_id
                driver.execute_script('window.open(' + user_id_url + ',"_blank");')
                src = driver.find_element_by_xpath('//*[@class="be6sR"]').get_attribute("src")
                response = requests.get(src)
                file = open('Profile Data/' + user_id + '.png', "wb")
                file.write(response.content)
                file.close()
                driver.execute_script('''window.close();''')

            except:
                # Class if u following
                user_id_url = 'https://www.instagram.com/' + user_id
                driver.execute_script('window.open(' + user_id_url + ',"_blank");')
                src = driver.find_element_by_xpath('//*[@class="_6q-tv"]').get_attribute("src")
                response = requests.get(src)
                file = open('Profile Data/' + user_id + '.png', "wb")
                file.write(response.content)
                file.close()
                driver.execute_script('''window.close();''')
                """

        except:
            break

    acc_you_follow.close()


def get_acc_following_you():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(
        executable_path=r'DevChrome Data\chromedriver.exe',
        options=options)

    acc_following_you = 'https://www.instagram.com/accounts/access_tool/accounts_following_you'
    driver.get(acc_following_you)

    acc_following_you = open(r'Synced Data/acc_following_you.txt', 'w')

    while True:
        try:
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='sqdOP  L3NKy   y3zKF     ']"))).click()
        except:
            break

    xpath = "//div[@class='-utLf']"
    idx = 1  # here first class's index is 1 not 0, cuz its positioning not index
    while True:
        try:

            xpath_new = xpath + "[" + str(idx) + "]"
            user_id = driver.find_element_by_xpath(xpath_new).get_attribute('innerHTML')
            idx += 1
            acc_following_you.write(user_id + '\n')

        except:
            break

    acc_following_you.close()
