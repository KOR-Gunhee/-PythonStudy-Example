#!/usr/bin/env python
# coding: utf-8

# In[101]:


import numpy as np

A = np.array([[1, 2], [3, 4]])
print(A.shape)

B = np.array([[5, 6], [7, 8]])
print(B.shape)

np.dot(A, B)

