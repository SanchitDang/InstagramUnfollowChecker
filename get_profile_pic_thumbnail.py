import requests
import time
from selenium import webdriver

# JAVASCRIPT document.getElementsByClassName("rkEop")[0].innerHTML
# src = driver.find_element_by_xpath('//*[@class="_6q-tv"][1]').get_attribute("src")


def get_image():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(
        # executable_path=r'DevChrome Data\chromedriver.exe',
        options=options)

    f5 = open(r'synced_data/not_following_back.txt', 'r')
    not_following_back_list = f5.readlines()

    for user in not_following_back_list:
        user_id = user[:-1]
        print(user_id)
        user_id_url = 'https://www.instagram.com/'+user_id
        print(user_id_url)
        driver.get(user_id_url)

        try:
            # Class if u not following
            src = driver.find_element_by_xpath('//*[@class="be6sR"]').get_attribute("src")
            response = requests.get(src)
            file = open('Profile Data/' + user_id + '.png', "wb")
            file.write(response.content)
            file.close()

        except:
            # Class if u following
            src = driver.find_element_by_xpath('//*[@class="_6q-tv"]').get_attribute("src")
            response = requests.get(src)
            file = open('Profile Data/' + user_id + '.png', "wb")
            file.write(response.content)
            file.close()


def get_image_without_loop():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(
        # executable_path=r'DevChrome Data\chromedriver.exe',
        options=options)

    user_id = 'itzzsanchit'
    user_id_url = 'https://www.instagram.com/' + user_id
    driver.get(user_id_url)

    try:
        # Class if u not following
        src = driver.find_element_by_xpath('//*[@class="be6sR"]').get_attribute("src")
        response = requests.get(src)
        file = open('Profile Data/' + user_id + '.png', "wb")
        file.write(response.content)
        file.close()

    except:
        # Class if u following
        src = driver.find_element_by_xpath('//*[@class="_6q-tv"]').get_attribute("src")
        response = requests.get(src)
        file = open('Profile Data/' + user_id + '.png', "wb")
        file.write(response.content)
        file.close()

    """    if driver.find_element_by_xpath('//*[@class="rkEop"]').get_attribute("innerHTML") == 'This Account is Private':
            # Class if u not following
            src = driver.find_element_by_xpath('//*[@class="be6sR"]').get_attribute("src")
            response = requests.get(src)
            file = open('Profile Data/' + user_id + '.png', "wb")
            file.write(response.content)
            file.close()
        else:
            # Class if u following
            src = driver.find_element_by_xpath('//*[@class="_6q-tv"]').get_attribute("src")
            response = requests.get(src)
            file = open('Profile Data/' + user_id + '.png', "wb")
            file.write(response.content)
            file.close()"""

