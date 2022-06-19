from bs4 import BeautifulSoup
import requests
import time

def main():
    html_content = requests.get('https://www.bbc.com/sport/football').text
    soup = BeautifulSoup(html_content, 'lxml')

    articles = soup.find_all('div', class_="gs-c-promo-body gs-u-mt@m gel-1/2@xs gel-1/1@m")

    article_title = []
    article_age = []
    for article in articles:
        try:
            age = article.find('span', class_="qa-status-date-output").text
            if 'd' in age:
                age = int(age[:-1]) *24
            elif 'h' in age:
                age = int(age[:-1])
            else:
                continue
            article_age.append(age)
            title = article.find('h3', class_="gs-c-promo-heading__title gel-pica-bold sp-o-link-split__text").text
            article_title.append(title)

        except AttributeError:
            break

    for i in range(len(article_title)):
        print(f"Title: {article_title[i]}".strip())
        print(f"How long since last updated: {article_age[i]} hours".strip())
        print()

    print("-------------------------------------------")
    print("-------------------------------------------")
if __name__ == '__main__':
    while True:
        main()
        time.sleep(10000)
