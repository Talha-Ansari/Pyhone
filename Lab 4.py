#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lecture 4


# In[2]:


s="University of central punjab"
type(s)


# In[3]:


print(s)


# In[4]:


s


# In[5]:


s[0:10]
s[0:20]


# In[6]:


s[0:10:2]


# In[7]:


s[30:0:-1]


# In[8]:


s[0:40]


# In[9]:


s[-5:]


# In[10]:


s[-15:-1:2]


# In[11]:


s[-15::2]


# In[15]:


city=" Lahore"
ucp =s+ city
ucp


# In[16]:


ucp.lower()


# In[17]:


ucp.upper()


# In[18]:


ucp


# In[19]:


len(ucp)


# In[22]:


ucp.split('i')


# In[23]:


ucp.split(" ")


# In[99]:


ucpHistory ="On 15 August 1996, The Punjab Group of Colleges petitioned Government of Punjab for the establishment of a university in the province. \Punjab Institute of Computer Science (PICS), Punjab College of Commerce (PCC), Punjab Law College (PLC) and Punjab College of Information Technology (PCIT) formed the core of the university at the time of establishment.Following a restructuring in 2004, the PCBA and PICS operate under the Faculty of Management Studies and Faculty of Information Technology of the University of Central Punjab respectively. The Punjab Colleges of Commerce and the Punjab Law College respectively function under the Faculties of Commerce and of Law of the University of Central Punjab. The Faculty of Engineering (FOE) was introduced in 2002."
ucpHistory.split(" ")


# In[90]:


#Task 1
length=len(ucpHistory)
counter=0
for x in range(length):
   if ucpHistory[x]>='a'and ucpHistory[x]<='z' or ucpHistory[x]>='A'and ucpHistory[x]<='Z':
    counter+=1
counter


# In[109]:


length=len(ucpHistory)
a=" "
counter=0
for x in range(length-1):
   if ucpHistory[x]!='o'and ucpHistory[x+1]!='f' or ucpHistory[x]!='f' and ucpHistory[x-1]!='o' :
    print( ucpHistory[x])


# In[106]:


ow=ucpHistory.split("of")
for x in range (30):
    print (ow[x], end =" ")


# In[97]:


ucpHistory=ow
print(ow)


# In[ ]:




