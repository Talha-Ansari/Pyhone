#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world")
x=5
y=3.4
print(x)
type(x)


# In[2]:


z=x+y
print(x, "+",y,"=",z)

name="Talha"
print(name)
type(name)


# In[3]:


x=int(input("Enter a x value: \n"))
y=float(input("Enter a y value : \n"))
print(x, "+",y,"=",x+y)


# In[4]:


type(x)
type(y)


# In[5]:


x=22
y=7
print(x/y,"\n",x//y)


# In[6]:


print("multiply",2*3)
print("power",2**3)


# In[7]:


#Ansari
'''
Talha
Khalid
'''


# In[8]:


True and False


# In[13]:


x=int(input("Plz enter a number : \n"))
if x>0:
    print("Its true")
    print ("X greater than 0 \nOHH Yes")
else:
    print("OHH No")
    print ("X is less than 1")
    print("Tu mara put choti kar")


# In[11]:


x=int(input("Enter a x value: \n"))
y=int(input("Enter a y value : \n"))
if x>y:
    print ("X greater than y")
elif y>x:
    print("y greater than x")
else:
    print("X is equal to y")


# In[12]:


x=int(input("Enter between 0 to 35 \n"))
if x>-1 and x<=9:
    print(x)
else:
    print(chr(x+55))


# In[14]:


x=int(input("Plz enter a number : \n"))
if x>0 and x<=9:
    print("Its true")
    print ("X greater than 0 \nOHH Yes")
else :
    print("OHH No")
    print ("X is greater than 9 or it is less than 1")
    print("Tu mara put choti kar")
    print("Tu mary level da nahi shoryya")
print("Thank You")


# In[16]:


for x in range(4):
    x=int(input("Enter between 0 to 35 \n"))
    if x>-1 and x<=9:
        print(x)
    else:
        print(chr(x+55))


# In[ ]:




