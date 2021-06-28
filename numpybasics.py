#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np


# In[21]:


sample_list=[4, 5, 6, "a"]
sample_list


# In[23]:


#Creating array
list_of_list=[[5, 6, 7], [8, 9, 10], [11, 12, 13]]
np.array(list_of_list)


# In[22]:


arr=np.array([4, 5, 6])
array


# In[9]:


#range of numbers -note python indexing starts from zero and last number will be excluded
np.arange(5, 20)


# In[11]:


np.arange(5, 20, 5)


# In[12]:


np.arange(5, 20, 5, dtype=float)


# In[102]:


np.zeros(10, dtype='float')


# In[13]:


np.ones(10, dtype=int)


# In[16]:


np.ones((3, 2))


# In[17]:


np.linspace(0, 20, 19)


# In[18]:


np.eye(3)


# In[19]:


np.random.randn(2, 3)


# In[20]:


np.random.randint(1, 10)


# In[25]:


a=np.random.rand(5,4)
a


# In[26]:


a.reshape(2, 10)


# In[32]:


b=np.random.randint(0, 50, 100)
c=b.reshape(10, 10)
c


# In[33]:


c.T


# In[36]:


c.max(), c.min(), c.argmin(), c.argmax()


# In[64]:


a=np.random.randn(5, 20)
a.shape
a.reshape(10, 10)


# In[66]:


B=np.random.rand(5, 20)
B


# In[70]:


C=np.random.randint(5, 20, 100)
C.reshape(10, 10)


# In[74]:


D=np.random.randint(5, size=(10, 10))
D


# In[75]:


matrix=np.array(([1, 2, 3, 4], [5, 6, 7, 8], [9,10, 11, 12]))
matrix


# In[76]:


matrix[0][3]


# In[77]:


matrix[:, 0]


# In[79]:


matrix[1:3, 1:3]


# In[84]:


array=np.arange(5, 11)
array


# In[86]:


bool=array<8
bool


# In[87]:


np.sqrt(array)


# In[88]:


np.log(array)


# In[89]:


np.exp(array)


# In[94]:


array1=np.arange(5, 11)
array2=np.arange(12, 18)
a=array1.reshape(2, 3), b=array2.reshape(3, 2)


# In[100]:


np.std(a), np.var(a), 


# In[101]:


sports=np.array(['golf', 'cric', 'fball', 'fball', 'cric'])
np.unique(sports)


# In[ ]:




