#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import tree


# In[2]:


X=[[0,0],[1,1]]
Y=[0,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)


# In[3]:


clf.predict([[2., 2.]])


# In[4]:


clf.predict([[3., 3.]])


# In[5]:


clf.predict([[3., 2.]])


# In[6]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer, StandardScaler
import pandas as pd
import numpy as np
data = pd.read_csv("F:\MLWS\ML0516deen.csv", encoding='utf-8', dtype=str, keep_default_na=False)
sc=StandardScaler()
df=data


# In[7]:


X=np.array(pd.DataFrame(data, columns=['ProgramName',
     'isWorkingTime',
     'obj_creationTime','obj_fileName','obj_fileSize','obj_isHidden','obj_lastWriteTime',
    'errorCode','functionName','returnValue',
    'subj_creationTime','subj_fileName','subj_fileSize','subj_isHidden','subj_lastWriteTime',
    'companyName','fileDescription','fileVersion','internalName','legalCopyright',
    'originalFilename','productName','productVersion','Permit?']))
y=np.array(pd.DataFrame(data, columns=['Permit?']))
X_train, X_test, y_train, y_test= train_test_split(X,y)


# In[8]:


X_train
sc.fit(X_train)
X_train_scaled=sc.transform(X_train)
X_test_scaled=sc.transform(X_test)
X_train=X_train_scaled
X_test=X_test_scaled
X_train


# In[ ]:


dt=DecisionTreeClassifier()
dt=dt.fit(X_train, y_train)


# In[ ]:


dt_predict=dt.predict(X_test)


# In[ ]:


feature_names=data.columns.tolist()
feature_names=feature_names[0:17]
target_name=np.array(['Group_A', 'Group_B'])


# In[ ]:


import pydotplus  
from IPython.display import Image
from sklearn import tree


# In[ ]:


dt_dot_data = tree.export_graphviz(dt, out_file = None,
                                  feature_names = feature_names,
                                  class_names = target_name,
                                  filled = True, rounded = True,
                                  special_characters = True)


# In[ ]:


dt_graph = pydotplus.graph_from_dot_data(dt_dot_data)


# In[ ]:


import os
#os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'


# In[ ]:


Image(dt_graph.create_png())


# In[ ]:


print(data)
print(type(data))


# In[ ]:


print(df)
print(data)
target=data.pop("Permit_Deny")

#tmp=df['TF']

print(data)


# In[ ]:


x_train, x_valid, y_train, y_valid = train_test_split(data, target, test_size=0.2, shuffle=True, stratify=target, random_state=42)


# In[ ]:


print(data)
print(target)
print(x_train)


# In[ ]:


tree=DecisionTreeClassifier(random_state=0)
tree.fit(x_train, y_train)


# In[ ]:


print("훈련 세트 정확도: {:.3f}".format(tree.score(x_train, y_train)))


# In[ ]:


print("테스트 세트 정확도: {:.3f}".format(tree.score(x_valid, y_valid)))


# In[ ]:


tree = DecisionTreeClassifier(max_depth=10, random_state=0)
tree.fit(x_train, y_train)
dtt=tree


# In[ ]:


print("훈련 세트 정확도: {:.3f}".format(tree.score(x_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(tree.score(x_valid, y_valid)))


# In[ ]:


from sklearn import tree


# In[ ]:


dt_dot_data = tree.export_graphviz(dtt, out_file = None,
                                  feature_names = feature_names,
                                  class_names = target_name,
                                  filled = True, rounded = True,
                                  special_characters = True)
dt_graph = pydotplus.graph_from_dot_data(dt_dot_data)
Image(dt_graph.create_png())


# In[ ]:


dot_data=export_graphviz(clf, 
                              out_file=None,
                             feature_names=df.feature_names,
                             class_names=df['Permit_Deny'],
                             filled=True,
                             rounded=True,
                             special_characters=True)
graph=graphviz.Source(dot_data)


# In[ ]:




