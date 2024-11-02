from selenium import webdriver
from time import sleep

def unfollow_asses():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(options=options)

    # Unfollow multiple
    with open(r'synced_data\not_following_back.txt', 'r') as not_following_back_data:
        total_user_names = len(not_following_back_data.readlines())
        not_following_back_data.seek(0)
        for i in range(total_user_names):
            user_name = not_following_back_data.readline()
            user_name_without_newline = user_name[:-1]
            driver.get('https://www.instagram.com/' + user_name_without_newline)
            try:
                sleep(2)
                driver.find_element_by_xpath('//span[@aria-label="Following"]').click()
                sleep(1)
                driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
                sleep(2)
            except:
                pass
