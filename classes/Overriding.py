#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Skills():
    def __init__(self):
        pass
    def msg(self):
        print("so you have the skills!")


# In[19]:


class HR():
    def __init__(self):
        super(HR, self).__init__()
    def msg(self):
        print("Good luck another time, you don't have the skills needed!")


# In[23]:


communication = HR()


# In[24]:


communication.msg()


# In[ ]:



