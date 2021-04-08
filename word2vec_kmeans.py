#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gensim.models.word2vec import Word2Vec

import warnings
warnings.filterwarnings("ignore")


# In[2]:


import pandas as pd
data = pd.read_csv('F:\MLWS\hirebat5tmp`.csv', encoding='utf-8', dtype=str, keep_default_na=False)


# In[3]:


data.head()


# In[4]:


P=data.pop('PN')
E=data.pop('B')
'''
A=data.pop('A')
B=data.pop('B')
C=data.pop('C')
D=data.pop('D')
F=data.pop('F')
G=data.pop('G')
H=data.pop('H')
'''
PN=pd.concat([P,E],axis=1)
'''
PN=data.pop('PN')
'''


# In[5]:


print(PN)


# In[6]:


sentences=PN.values.tolist()


# In[7]:


from gensim.models import Word2Vec
print(sentences)
w2v =Word2Vec(sentences, size=100, window=5, min_count=0, workers=32, sg=1)
print(w2v)
#print(w2v.wv.most_similar("C:\\Program Files\\Microsoft Office\\Root\\Office16\\WINWORD.EXE"))


# In[8]:


from sklearn.cluster import KMeans
import numpy as np
word_vectors = w2v.wv.syn0 # 어휘의 feature vector
num_clusters = int(word_vectors.shape[0]/50) # 어휘 크기의 1/5나 평균 5단어
print(num_clusters)
num_clusters = int(num_clusters)
num_clusters=2


# In[9]:


kmeans_clustering = KMeans(n_clusters=num_clusters)
idx = kmeans_clustering.fit_predict(word_vectors)


# In[10]:


idx = list(idx)
names = w2v.wv.index2word
word_centroid_map = {names[i]: idx[i] for i in range(len(names))}


# In[11]:


for c in range(num_clusters):
    # 클러스터 번호를 출력
    print("\ncluster {}".format(c))
    
    words = []
    cluster_values = list(word_centroid_map.values())
    for i in range(len(cluster_values)):
        if (cluster_values[i] == c):
            words.append(list(word_centroid_map.keys())[i])            
    print(words)


# In[12]:


vectors=w2v.wv.vectors
names=w2v.wv.index2word


# In[13]:


from scipy.spatial import distance_matrix
distance = distance_matrix(vectors, vectors)

distance_df = pd.DataFrame(distance, columns=names, index=names)


# In[14]:


from sklearn.feature_extraction.text import CountVectorizer
vec=CountVectorizer()
X=vec.fit_transform(set(PN))


# In[ ]:





# In[ ]:




