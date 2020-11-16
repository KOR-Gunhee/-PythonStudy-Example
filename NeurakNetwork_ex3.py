#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
X = np.array([1.0, 0.5])
print(X.shape)

W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
print(W1.shape)

B1 = np.array([0.1, 0.2, 0.3])
print(B1.shape)

A1 = np.dot(X, W1) + B1
print(A1)

Z1 = sigmoid(A1)
print(Z1)


