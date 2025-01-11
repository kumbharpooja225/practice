#!/usr/bin/env python
# coding: utf-8

# In[4]:


def calArea(r):
    a=3.14*r*r
    return a


# In[5]:


calArea(r=40)


# In[8]:


w=calArea(r=23)
w


# In[9]:


type(w)


# In[11]:


def aor(l,w):
    a=l*w
    return a
aor(5,6)


# In[12]:


aor(10,5)


# In[16]:


def agg(l,b,r):
    rec=l*b
    cir=3.14*r**2
    return rec,cir
area(5,4,3)


# In[17]:


c=agg(4657,787,3456)
c


# In[18]:


t='hyd 500078 telangana'
t


# In[34]:


for a in t:
    b=t.count(a)
print(b)


# In[43]:


def countA(x):
    d=x.lower()
    return d.count('')
    


# In[44]:


countA(t)


# In[45]:


for int in t:
    c=t.count(int)


# In[46]:


c


# In[48]:


def count_num_alpha(x):
    c=0
    d=0
    for i in x:
        if i.isalpha():
            c+=1
        elif i.isnumeric():
            d+=1
            
    return{"no. of alphabets":c,"no. of digits":d}


# In[50]:


count_num_alpha(t)


# In[ ]:




