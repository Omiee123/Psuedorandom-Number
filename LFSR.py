#!/usr/bin/env python
# coding: utf-8

# In[2]:


def XOR_fun(array):
    i=0
    result=0
    while i < len(tap)-1:
        if i == 0:
            result = 1 if int(array[tap[0]-1]) != int(array[tap[1]-1]) else 0
            i = i + 2
            #print(result)
        else:
            result = 1 if result != int(array[tap[i]-1]) else 0
            i = i + 1
            #print(result)
            
    return result


# In[3]:


n = input("Enter the initial value : ")
print("Enter the tap value :")
tap = [ int(i) for i in input().split() ]


# In[4]:


ite_n = []
ite_n.append(n)


# In[6]:


val = XOR_fun(ite_n[0])    
#shift register
rand_num = str(val)+str(ite_n[0][0:len(n)-1])
ite_n.append(rand_num)

i = 1


# In[10]:


while ite_n[i] != n:
    #XOR of tap value
    val = XOR_fun(ite_n[i])
    
    #shift register
    rand_num = str(val)+str(ite_n[i][0:len(n)-1])
    i = i + 1 
    ite_n.append(rand_num)


# In[11]:


print("The Random Number Generated are "+str(ite_n))
print("The Period of the Initial seed given is "+str(i))


# In[ ]:




