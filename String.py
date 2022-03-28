#!/usr/bin/env python
# coding: utf-8

# In[20]:


a="Hello World"
print(a)
a="My name is Talha"
print(a[0])
print("Talha" in a)


# In[29]:


for x in a:
    print(x,end='')
print("\n")
for x in a:
    if x=='a':
        print(x)


# In[117]:


b=a
b=b.split(" ")
print (b,"\n",a)


# In[30]:


print(len(a))


# In[148]:


c=''
if "Talha" in a:
    print(a)
for x in b:
    if "Talha"not in x:
        c+=x
        print(x)
c


# In[52]:


print(a)
a[-1::-1]


# In[53]:


a.strip()


# In[55]:


print(a.replace('a','i'))
print(a)


# In[72]:


age=22
print(a+" "+str(age))
x=input("Enter ur name")
sent="My name is {} and my age is {}"

print(sent.format(x,age))


# In[86]:


txt = 'We are\'s gona \"enjoy\" this' 
print(txt)


# In[101]:


print(a)
print(a.capitalize())
print(a.casefold())
print(a.center(5,"x"))
print(a.count('a'))
print(a.encode())


# In[155]:


str2 = ''
a=0
print(len(b))
for i in b:
    if "is" not in i:
        str2 = str2 + i
        a=1
    if a==1:
        str2+=" "
        a=0
    
print("The Final String : Str2  = ", str2)


# In[ ]:




