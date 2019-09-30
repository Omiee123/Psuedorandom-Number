#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Middle Digit Depends on the length of seed value

n = int(input("Enter the Initial Seed Value :"))
len_n = len(str(n))
num = int(input("Enter the no of Random Numbers you want :"))


# In[2]:


print(len_n)
output = [0]*num


# In[3]:


output[0]=n


# In[4]:


output


# In[15]:


for i in range(num-1):
    sq_n = output[i]*output[i]
    len_nn = len(str(sq_n))
    len_thres = int((len_nn - len_n)/2)
    temp = str(sq_n)[len_thres:-len_thres]
    output[i+1] = int(temp)


# In[16]:


output

