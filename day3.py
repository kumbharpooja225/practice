#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=55


# In[2]:


a


# In[4]:


a=[22,11,5,56]
a


# In[4]:


a='india'
a


# In[5]:


a.upper()


# In[6]:


a


# In[8]:


a.isdigit()


# In[13]:


d


# In[15]:


d= {101:200,
  102:600,
  103:(30,40,50,60,70),
  104:(1000,5000,5500,6000,7000,56),
  106:'4000',
  107:'india'}

  


# In[16]:


d[107].upper()


# In[17]:


d[107].lower()


# In[20]:


d[104].append(2.2345)


# In[21]:


type(d)


# In[22]:


type(104)


# In[24]:


{101 : {50: [7,8,9,10], 'apple': (20,10,70,[90,180,270])},
 102:600,
 103:(30,40,50,60,70),
 106:4000,
 107:'india'
}


# In[3]:


x=int(input())
if x/4 and x/100:
    print("leap year")
else:
    print("not a leap year")


# In[9]:


a=input()
if a.startswith("T" and "t"):
    print("true")
else:
    print("False")


# In[16]:


x="mp"
if x.startswith('m' or 'l'):
    print("s")
else:
    print("n")


# In[30]:


x="sikkim"
if x[0].lower() in ('s','d','h')  :
    print("S")
else:
    print("No")


# In[ ]:




