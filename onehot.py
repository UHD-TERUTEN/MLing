#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer

data = pd.read_csv('F:\MLWS\index4train.csv', encoding='utf-8', dtype=str, keep_default_na=False)


# In[2]:


data.values.tolist()
data=data.values.tolist()
print(data)


# In[3]:


onehot=tf.keras.utils.to_categorical(data, 15165)
print(onehot)


# In[ ]:




