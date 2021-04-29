#!/usr/bin/env python
# coding: utf-8

# <h1>Peer-graded Assignment: Segmenting and Clustering Neighborhoods in Toronto</h1>
# 
# 

# <h2>Importing libraries</h2>

# In[12]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# <h2>Getting the website</h2>

# <h2>Webscraping</h2>
# <p>Table content of the webpage are stored in a new data frame</p>
# 

# In[33]:


url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
website = requests.get(url)
website = website.text
soup = BeautifulSoup(website,'lxml')




# <h2>WebScraping</h2>
# <p>Data from the page table are inserted into a new dataframe</p>

# In[92]:



Neighborhoods = []
df = pd.DataFrame({'PostalCode':[""],"Borough":[""],"Neighborhood" : [""]})
df = df.drop(df.index[0])

table=soup.find('table')
for row in table.findAll('td'):
    if row.span.text=='Not assigned':
        pass
    else:
     postalCode = row.p.text[:3]
     Borough = (row.span.text).split('(')[0]
     Neighborhood = (((((row.span.text).split('(')[1]).strip(')')).replace(' /',',')).replace(')',' ')).strip(' ')
     df = df.append({'PostalCode': postalCode,"Borough":Borough,"Neighborhood":Neighborhood}, ignore_index=True)


# <h2>Data about the table are displayed</h2>

# In[96]:


df.head()


# In[104]:


rows = df.shape[0]
print("The number of rows = " + str(rows))

