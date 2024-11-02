from selenium import webdriver
from time import sleep

# inc_in_progress = 0


def unfollow_asses():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(options=options)

    # Unfollow multiple
    with open(r'synced_data\not_following_back.txt', 'r') as not_following_back_data:
        # global inc_in_progress
        total_user_names = len(not_following_back_data.readlines())
        # inc_in_progress = 100 / total_user_names
        not_following_back_data.seek(0)
        for i in range(total_user_names):
            user_name = not_following_back_data.readline()
            user_name_without_newline = user_name[:-1]
            driver.get('https://www.instagram.com/' + user_name_without_newline)
            try:
                sleep(2)
                # driver.save_screenshot("ss"+str(i)+".png")
                driver.find_element_by_xpath('//span[@aria-label="Following"]').click()
                sleep(1)
                driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
                # inc_in_progress += inc_in_progress
                # OR (EASY), split gui_main into functions
                # gui_main.my_progress['value'] += inc_in_progress
                sleep(2)
            except:
                pass
