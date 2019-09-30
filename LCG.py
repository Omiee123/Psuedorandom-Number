#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Linear Congruential Generator")
print("X(n+1) = (ax(n)+c)modM")
a = int(input("Enter a :"))
c = int(input("Enter c :"))
m = int(input("Enter M :"))
x = []
val = int(input("Enter Initial Seed Value :"))


# In[2]:


x.append(val)
temp = x[0]


# In[3]:


i=0


# In[5]:


comp = ((a*x[0])+c)%m
x.append(comp)


# In[7]:


if comp == temp:
    p = 1
else:
    i = i+1


# In[8]:


while temp != comp:
    comp = ((a*x[i])+c)%m
    #print(comp,i)
    x.append(comp)
    i = i+1


# In[9]:


print("The Period of LCG is "+str(i))
print("The Random Number for the given values are"+str(x))


# In[ ]:




