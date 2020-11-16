#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Man:
    def __init__(self, name):
        self.name = name
        print("Initialiced!")
        
    def hello(self):
        print("Hellp "  + self.name + "!")
        
    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()

