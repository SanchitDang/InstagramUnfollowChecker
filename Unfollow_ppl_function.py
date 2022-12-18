from selenium import webdriver
from time import sleep

# inc_in_progress = 0


def unfollow_asses():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    # specify the path to chromedriver.exe (download and save on your computer)
    driver = webdriver.Chrome(executable_path='DevChrome Data/chromedriver.exe', options=options)

    # Unfollow multiple
    with open(r'Synced Data\not_following_back.txt', 'r') as assholes:
        # global inc_in_progress
        total_user_names = len(assholes.readlines())
        # inc_in_progress = 100 / total_user_names
        assholes.seek(0)
        for i in range(total_user_names):
            user_name = assholes.readline()
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
