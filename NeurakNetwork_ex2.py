#!/usr/bin/env python
# coding: utf-8

# In[117]:


import numpy as np

X = np.array([1.0, 0.5])
print(X.shape)

W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
print(W.shape)

B1 = np.array([0.1, 0.2, 0.3])
print(B1.shape)

A1 = np.dot(X, W1) + B1
print(A1)

