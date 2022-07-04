import feedparser

#Regular news from Aftonbladet
url_regular_news = 'https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/'
url_Sports_news = 'https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt/sport/'
url_culture_news = 'https://rss.aftonbladet.se/rss2/small/pages/sections/kultur/'
url_entertainment_news = 'https://rss.aftonbladet.se/rss2/small/pages/sections/nojesbladet/'




f = feedparser.parse(url_entertainment_news)
#To get entriees
print(f.entries)
print(f.href)

#print(len(f.entries))

RegulNews_key = 'RegularNews'
SportNews_key = "SportNews"
CultNews_key = 'CultNews'
Entertainment_key = 'EnterainmentNews'

#Get Title and Link for each New entry:
#Iterates through all entries
for entry in f.entries:
        if f.href == url_regular_news:
            print(entry.title)
            print(entry.link)
            print("--------------------------")
        elif f.href == url_Sports_news:
            print(entry.title)
            print(entry.link)
            print("--------------------------")
        elif f.href == url_culture_news:
            print(entry.title)
            print(entry.link)
            print("--------------------------")
        elif f.href == url_entertainment_news:
            print(entry.title)
            print(entry.link)
            print("--------------------------")
        else:
            print("Printing invalid data")


#Write to a File either CSV or regular Text file


"""
fileToWrite = open("test.txt", "w")
fileToWrite.write(pageSource)
fileToWrite.close()
fileToRead = open("test.txt", "r")
print(fileToRead.read())
fileToRead.close()
driver.quit()
"""