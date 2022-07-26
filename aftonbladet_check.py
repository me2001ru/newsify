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
driver.get("https://www.aftonbladet.se/")

print(driver.title)

try:
    driver.find_element(By.CSS_SELECTOR, "//button[contains(@class,'message-component message-column')]").click()
except:
    print()
    print("click does not exist")
    print()