#!/usr/bin/env python
# coding: utf-8

# In[56]:


from bs4 import BeautifulSoup as BS
import requests

url = "https://en.wikipedia.org/wiki/"
data = requests.get(url)
soup = BS(data.text,"html.parser")
wiki = soup.find("div",class_ = "mw-parser-output").text

print (wiki)


# In[ ]:




