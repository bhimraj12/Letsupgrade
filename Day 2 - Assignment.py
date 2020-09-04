#!/usr/bin/env python
# coding: utf-8

# # list & It's default functions

# In[32]:


lst = ["Bhimraj",10,3932,35.43,[1,2,4]]


# In[33]:


lst


# In[6]:


lst[0]


# In[14]:


lst[4][1]


# In[16]:


lst.append("Apsit") 


# In[18]:


lst


# In[19]:


lst.index(35.43)


# In[21]:


lst[-1]


# In[28]:


lst[-7]


# In[26]:


lst[1]


# In[29]:


lst[-5][1]


# # Dictionary & It's Deflaut functions

# In[34]:


dit = {"name":"Bhimraj", "age":"19",
       "number":"8655552214","email":"bhimrajparihar0@gmail.com"}


# In[36]:


dit


# In[38]:


dit.get('name')


# In[40]:


dit["name"]


# In[42]:


dit.items()


# In[44]:


dit.keys()


# In[46]:


dit.pop("name")


# In[48]:


dit


# In[50]:


dit["College"] = "APSIT"


# In[52]:


dit


# In[54]:


type(dit)


# # Sets & It's default functions

# In[56]:


st = {"bhimraj","apsit",1,3,2,2,5,3,1,6,4,2}


# In[58]:


st


# In[59]:


st1 = {"bhimraj",1}


# In[61]:


st1.issubset(st)


# #  Tuple & It's Default functions

# In[62]:


tup = ("bhimraj","@","apsit")


# In[64]:


tup


# In[67]:


tup.count("@")


# In[71]:


tup.index("apsit")


# # Strings & It's default functions

# In[72]:


name = 'Raja'
name1 = 'Rani'


# In[74]:


name


# In[76]:


name + " " + name1


# In[77]:


type(name)

