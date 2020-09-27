#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup as bs4


# In[10]:


import requests


# In[11]:


url = "https://www.animenewsnetwork.com/"


# In[12]:


html = requests.get(url).text


# In[13]:


main_soup = bs4(html,"html.parser")


# In[14]:


news_box = main_soup.find_all('div',{"class":"herald box news"})


# In[15]:


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
    
    


# In[ ]:




