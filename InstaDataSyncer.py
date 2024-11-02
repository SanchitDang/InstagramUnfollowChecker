from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# Array to store collected texts
all_texts = []
all_texts2 = []

# Find the target div element
target_div_selector = "div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6"
acc_you_follow = open(r'Synced Data/acc_you_follow.txt', 'w')
acc_following_you = open(r'Synced Data/acc_following_you.txt', 'w')

def scroll_div_and_collect(num):
    global all_texts

    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(
        options=options)
    
    # Find the target div element
    target_div = driver.find_element(By.CSS_SELECTOR, target_div_selector)

    # Select all span elements with the specified class inside the target div
    spans = target_div.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")

    # Collect text from each span and add it to the array if not already present
    for span in spans:
        text_content = span.text.strip()
        if text_content and text_content not in all_texts:
            all_texts.append(text_content)
            acc_you_follow.write(text_content + '\n')
            if len(all_texts) >= num:
                print("Reached", num, "users. Stopping collection:", all_texts)
                return  # Exit the function if 10 unique texts are collected

    # Check if the length of collected texts is 10
    if len(all_texts) >= num:
        print("Reached", num, "users. Stopping collection:", all_texts)
        return  # Exit the function if 10 unique texts are collected

    # Scroll the div by its height
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", target_div)

    # Wait for new content to load
    time.sleep(1)  # Adjust timeout as needed

    # Check if more content can be loaded in the div and continue scrolling
    if target_div.get_attribute('scrollHeight') > target_div.get_attribute('scrollTop'):
        scroll_div_and_collect(num)
    else:
        # Scrolling is complete; log all collected texts
        print("Scrolling complete. All texts collected:", all_texts)

def scroll_div_and_collect2(num):

    global all_texts2
    print("scroll_div_and_collect2: ", len(all_texts2))

    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(
        options=options)
    
    # Find the target div element
    target_div = driver.find_element(By.CSS_SELECTOR, target_div_selector)

    # Select all span elements with the specified class inside the target div
    spans = target_div.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")

    # Collect text from each span and add it to the array if not already present
    for span in spans:
        text_content = span.text.strip()
        if text_content and text_content not in all_texts2:
            all_texts2.append(text_content)
            acc_you_follow.write(text_content + '\n')
            # Check if the length of collected texts is 10
            if len(all_texts2) >= num:
                print("Reached", num, "users. Stopping collection:", all_texts)
                return  # Exit the function if 10 unique texts are collected

    # Check if the length of collected texts is 10
    if len(all_texts2) >= num:
        print("Reached", num, "users. Stopping collection:", all_texts)
        return  # Exit the function if 10 unique texts are collected

    # Scroll the div by its height
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", target_div)

    # Wait for new content to load
    time.sleep(1)  # Adjust timeout as needed

    scroll_div_and_collect2(num)
    # Check if more content can be loaded in the div and continue scrolling
    # if target_div.get_attribute('scrollHeight') > target_div.get_attribute('scrollTop'):
    #     scroll_div_and_collect2(num)
    # else:
    #     # Scrolling is complete; log all collected texts
    #     print("Scrolling complete. All texts collected:", all_texts2)

# Functions
def get_acc_you_follow():
    pass

def get_acc_you_follow2():

    following_count=0

    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    driver = webdriver.Chrome(
        options=options)

    acc_you_follow = 'https://www.instagram.com/sannnchit_/'
    driver.get(acc_you_follow)

    # acc_you_follow = open(r'Synced Data/acc_you_follow.txt', 'w')
    time.sleep(2)

    ### GETTING FOLLOWING COUNT
    try:
        # Wait for the span element to be present and select all elements with the given class
        spans = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
        )

        # Get the text of the first span and convert it to a number
        if spans:
            following_text = spans[2].text.strip().replace(",", "")
            follwoing = int(following_text)

            # Print the result
            print("The following count is:", follwoing)
            following_count = follwoing
        else:
            print("No span elements with the specified class were found.")        
    except Exception as e:
        print("An error occurred:", e)
    time.sleep(2)

    ### CLICKING ON FOLLOWING
    try:
        # Wait for the <a> element with the specified href attribute to be present and clickable
        target_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/sannnchit_/following/"]'))
        )
        # Click the <a> element
        target_link.click()
    except Exception as e:
        print("An error occurred:", e)
    time.sleep(2)

    scroll_div_and_collect(following_count)    


def get_acc_following_you():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    following_count2=0

    driver = webdriver.Chrome(
        
        options=options)

    acc_following_you = 'https://www.instagram.com/sannnchit_/'
    driver.get(acc_following_you)

    # acc_following_you = open(r'Synced Data/acc_following_you.txt', 'w')
    time.sleep(2)

    ### GETTING FOLLOWING COUNT
    try:
        # Wait for the span element to be present and select all elements with the given class
        spans = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
        )

        # Get the text of the first span and convert it to a number
        if spans:
            first_span_text = spans[1].text.strip().replace(",", "")
            first_span_number = int(first_span_text)

            # Print the result
            print("The first span's text as a number:", first_span_number)
            following_count2 = first_span_number
        else:
            print("No span elements with the specified class were found.")        
    except Exception as e:
        print("An error occurred:", e)
    time.sleep(2)

    ### CLICKING ON FOLLOWING
    try:
        # Wait for the <a> element with the specified href attribute to be present and clickable
        target_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/sannnchit_/followers/"]'))
        )
        # Click the <a> element
        target_link.click()
    except Exception as e:
        print("An error occurred:", e)
    time.sleep(2)

    scroll_div_and_collect2(following_count2)  
