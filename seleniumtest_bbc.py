from tkinter import N
from pyparsing import empty
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.bbc.com/")

print(driver.title)

links = driver.find_elements(By.XPATH, "//a[contains(@class,'block-link__overlay-link')]")
all_links_in = []
for title in links:
    all_links_in.append(title.get_attribute("href"))

for link in all_links_in:
    print(f"Checking link nr: {link}")
    if "live" in link or "Live" in link:
        continue
    # print(link)
    driver.get(link)

    # check if css span to click
    try:
        if "live" in link or "Live" in link:
            continue
        driver.find_element(By.CSS_SELECTOR, "//button[contains(@class,'continue-button banner-button')]").click()
    except:
        print()
        print("click does not exist")
        print()

    try:
        text_found_in_article = driver.find_elements(By.XPATH, "//p[contains(@class,'ssrcss-1q0x1qg-Paragraph eq5iqo00')]")
        for section in text_found_in_article:
            print(section.text)
        print()
    except:
        print(f"\n=====could not find 'l' value, setting to empty string=====\n")
    finally:
        print()

driver.quit()
