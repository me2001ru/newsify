from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import feedparser
#Get the website with selenium and manipulate with BeautifulSoup

#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--incognito')
#options.add_argument('--headless')
#options.add_argument("--window-size=2560,10000")


#PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH, chrome_options=options)

url = 'https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/'

#dir(feedparser)
f = feedparser.parse(url)
#print(f)

#Feed and Entries
#All Keys of each feed
print(f.keys())
#print(f.headers)

#To get entriees
print(f.entries)


print(len(f.entries))


#Get Title and Link for each New entry:

for entry in f.entries:
    print(entry.title)
    print(entry.link)
    print("--------------------------")













#print(f['feed']['href'])


#print(f)

#d = feedparser.parse(url)
#d['feed']['title']




#driver.get(url)
#print(driver.page_source)

#pageSource = driver.page_source


#main_html_page = BeautifulSoup(pageSource, 'lxml')

#links = main_html_page.find_all("div", {"class": 'line'})

#for link in links:
#     list = link.find_next("span")
#     print(list)



#for link in list_links:
#    print(link)
#    print("-------------------------------------------------------")
"""


#//*[@id="folder2"]/div[2]/div[2]/span[2]

#//*[@id="folder5"]/div[2]/div[2]/span[2]/text()

























#driver.set_window_position(0, 0)
#driver.set_window_size(1024, 10000)
#Its purpose is for the contionus scrolling on a page.
#SCROLL_PAUSE_TIME = 0.5

# Get scroll height
#last_height = driver.execute_script("return document.body.scrollHeight")+4000
#print("The documents body height: ", last_height)

#driver.execute_script("window.scrollBy(0, 7000)")
#driver.scrollHeight()
#time.sleep(3)

#print(driver.title)
#print("----------------------------------")
#print(driver.page_source)

#artocles = driver.find_element(By.CLASS_NAME, "css-198qxnm")
#for articel in artocles:
#    print(articel.text)
#print(artocles.get_attribute('text'))
#element.get_attribute('text')



#If you wanna use some selenium code do it here
#html_page = driver.find_elements(By.CLASS_NAME, 'css-b082k8')


#Ther rest here is BeautifulSoup Code
page_source = driver.page_source
main_html_page = BeautifulSoup(page_source, 'lxml')
#print("You are not printing the entire page")
#print(main_html_page.prettify())

main_page = main_html_page.find("section", {"class": 'css-bo82k8'})

#print("-----------------")
#print(main_page.prettify())

#print("---------------------------")
#Get all newly news
print("Breaking news :")
breaking_news = main_page.find_all("a", {"class": "css-ihtb25"})

for news in breaking_news:
    print(news)
time.sleep(3)
#Regular News
print("Regular news: ")
regular_news = main_page.find_all("a", {"class":"css-826iu8"})
for news in regular_news:
    print(news)
time.sleep(3)


#This is for the sports articles
sports_articles = main_page.find_all("div", {"class":"css-1fks8v0"})

print("All Sports articles:")
for article in sports_articles:
    print(article)

"""





