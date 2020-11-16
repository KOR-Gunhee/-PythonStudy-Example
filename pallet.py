#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('pallet.png')

plt.imshow(img)
plt.show()

