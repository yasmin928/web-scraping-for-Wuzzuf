#!/usr/bin/env python
# coding: utf-8

# In[1]:


#iimport liberares
import requests 
from bs4 import BeautifulSoup 
import webbrowser  
import selenium 
import csv
from itertools import zip_longest
import pandas as pd


# In[2]:


job_title=[]
company_name=[]
locations_name=[]
skills=[]
links=[]


# In[3]:


#user request to fitch the url
result = requests.get('https://wuzzuf.net/search/jobs/?q=python&a=hpb')


# In[4]:


#save pge content/markup
src=result.content
#print(src)


# In[5]:


#create soup object to parse content
soup =BeautifulSoup(src,"lxml")
#print(soup)


# In[6]:


#find elements containing info we need
#job titiles,job skilles,company name,location name
#note:find_all return a list
job_titles =soup.find_all("h2",{"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
locations_names = soup.find_all("span",{"class":"css-5wys0k"})
job_skills =soup.find_all("div",{"class":"css-y4udm8"})
#print(job_titles)
#print(company_names)
#print(locations_names)
#print(job_skills)


# In[7]:


#crreate loop over returned lists to extreact needed info innto another list
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs["href"])
    company_name.append(company_names[i].text)
    locations_name.append(locations_names[i].text)
    skills.append(job_skills[i].text)
    


# In[8]:


#create csv file and fill it with values
#Note*means unpaking for the content
file_list =[job_title, company_name, locations_name , skills ,links  ]
exported = zip_longest(*file_list)
with open(r"C:\Users\GREEN\jobtest.csv" , "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title", "company name" , "location","skills","links"])
    wr.writerows(exported)


# In[ ]:





# In[ ]:





# In[ ]:




