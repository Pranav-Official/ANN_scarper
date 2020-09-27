

from bs4 import BeautifulSoup as bs4
import requests

url = "https://www.animenewsnetwork.com/"
html = requests.get(url).text
main_soup = bs4(html,"html.parser")
news_box = main_soup.find_all('div',{"class":"herald box news"})
count = 0
for box in news_box:
    count+=1
    title_h = box.find('div',{"class":"wrap"})
    title = title_h.div.h3.a.text
    time_h = box.find('div',{"class":"byline"})
    time = time_h.time.text
    descript = box.find('span',{"class":"full"}).text
    page_url = box.find('div',{"class":"wrap"}).div.h3.a['href']
    print(str(count) + "\n\n" , title + "\n\n" , time + "\n\n", descript + "\n\n", url + page_url[1:]+"\n\n\n")
    

