#!/usr/bin/env python
# coding: utf-8

# In[102]:


import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B.shape)

np.dot(A, B)

