from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Global configuration
username="_theitech_"
target_div_selector = "div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6"
span_selector = "span._ap3a._aaco._aacw._aacx._aad7._aade"

# Initialize file paths
acc_you_follow_file = r'synced_data/acc_you_follow.txt'
acc_following_you_file = r'synced_data/acc_following_you.txt'


def setup_driver():
    """Set up the WebDriver with debugging options."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    return webdriver.Chrome(options=options)


def collect_texts(driver, num, all_texts, file):
    """Scroll through the target div to collect unique text content."""
    target_div = driver.find_element(By.CSS_SELECTOR, target_div_selector)

    while len(all_texts) < num:
        spans = target_div.find_elements(By.CSS_SELECTOR, span_selector)
        for span in spans:
            text_content = span.text.strip()
            if text_content and text_content not in all_texts:
                all_texts.append(text_content)
                file.write(text_content + '\n')
                if len(all_texts) >= num:
                    print(f"Reached {num} users. Stopping collection:", all_texts)
                    return

        # Scroll and wait for new content to load
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", target_div)
        time.sleep(1)


def get_following_count(driver, span_index):
    """Retrieve the count of accounts followed or following based on the span index."""
    spans = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
    )
    return int(spans[span_index].text.strip().replace(",", "")) if spans else 0


def click_link(driver, link_xpath):
    """Click a link specified by the XPath."""
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, link_xpath))).click()
    time.sleep(2)


def get_acc_you_follow():
    """Collect accounts that the user is following."""
    driver = setup_driver()
    driver.get('https://www.instagram.com/'+username+'/')
    time.sleep(2)

    # Automatically get the number of accounts the user is following
    following_count = get_following_count(driver, 2)
    click_link(driver, '//a[@href="/'+username+'/following/"]')

    with open(acc_you_follow_file, 'w') as file:
        all_texts = []
        collect_texts(driver, following_count, all_texts, file)


def get_acc_following_you():
    """Collect accounts that follow the user."""
    driver = setup_driver()
    driver.get('https://www.instagram.com/'+username+'/')
    time.sleep(2)

    # Automatically get the number of accounts following the user
    followers_count = get_following_count(driver, 1)
    click_link(driver, '//a[@href="/'+username+'/followers/"]')

    with open(acc_following_you_file, 'w') as file:
        all_texts = []
        collect_texts(driver, followers_count, all_texts, file)
