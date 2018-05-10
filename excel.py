
# coding: utf-8

# In[35]:


import pandas as pd


# In[41]:


data = pd.read_excel("Links.xlsx", header = None , names = ['Links'])


# In[26]:


from bs4 import BeautifulSoup
import urllib.request as urllib


# In[45]:


urls = data["Links"]
sizes = []


# In[46]:


for url in urls:
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html , 'html.parser')
    size_box = soup.find('select', attrs={'class': 'form-control size-drop-down'})
    options = size_box.find_all('option' , attrs = {'class': "swatch-item "})
    size = []
    for option in options:
        size.append(option.text)
    sizes.append(size)


# In[48]:


data["Sizes"] = sizes


# In[51]:


data.to_excel("Linkswithsizes.xlsx")

