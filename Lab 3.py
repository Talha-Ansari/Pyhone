#!/usr/bin/env python
# coding: utf-8

# In[6]:


for x in range(10):
    print(x)


# In[7]:


for x in range(2,10,2):
    print(x)


# In[9]:


x=10
i=2
for x in range(i,x+1,2):
    print(x)


# In[12]:


x=0
i=50
for x in range(i,x,2*-1):
    print(x)


# In[13]:


x=0
i=50
for x in range(i,x,2*-1):
    print(x,end =" ")


# In[15]:


i=int(input("Enter a number : \n"))
for x in range(1,i):
    if x % 3==0:
        print(x,end=" ")


# In[16]:


x=int(input("Enter a number : \n"))
counter=0
for i in range(1,x+1):
    if x%i==0:
        counter+=1
if counter==2:
    print("This is a prime number : ",x)
else:
    print ("This is not a prime number : ",x)


# In[17]:


x=int(input("Enter a number : \n"))
i=x%10
if i%2==0:
    print(i , " is a prime number ")


# In[19]:


x=int(input("Enter a number : \n"))
even=0
odd=0
while x!=0:
    a=x%10
    x=x//10
    if a%2==0:
        even+=1
    else:
        odd+=1

print ("Even : ",even, " Odd ",odd)


# In[21]:


counter=0
for x in range(111,999,1):
    a=x
    counter=0
    while a!=0:
        if a%2!=0:
            counter+=1
        a//=10
    if counter==3:
        print(x,end=" ")
    
        
        


# In[23]:


def abc(a,b):
    print ("Hello World")
    return a+b
print(abc(1,2))


# In[24]:


def abc(a,b):
    print ("Hello World")
    return a+b,b
x,y=abc(5,10)
print (x,y)


# In[27]:


x,_=abc(5,10)
print(x,_)


# In[ ]:




