#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np

A = np.array([[1, 2], [3, 4]])
print(A)

print(A.shape)
print(A.dtype)

B = np.array([[3, 0], [0, 6]])
print(B)

print(A + B)

print(A * B)

print(A * 10)

