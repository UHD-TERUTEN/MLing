#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_entropy(df):
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value]/len(df[Class])
        entropy += -fraction*np.log2(fraction)
    return entropy


# In[2]:


def find_entropy_attribute(df,attribute):
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    target_variables = df[Class].unique()  #This gives all 'Yes' and 'No'
    variables = df[attribute].unique()    #This gives different features in that attribute (like 'Hot','Cold' in Temperature)
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
            den = len(df[attribute][df[attribute]==variable])
            fraction = num/(den+eps)
            entropy += -fraction*log(fraction+eps)
        fraction2 = den/len(df)
        entropy2 += -fraction2*entropy
    return abs(entropy2)


def find_winner(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:
#         Entropy_att.append(find_entropy_attribute(df,key))
        IG.append(find_entropy(df)-find_entropy_attribute(df,key))
    return df.keys()[:-1][np.argmax(IG)]

def get_subtable(df, node,value):
    return df[df[node] == value].reset_index(drop=True)


def buildTree(df,tree=None): 
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    
    #Here we build our decision tree

    #Get attribute with maximum information gain
    node = find_winner(df)
    
    attValue = np.unique(df[node])
    
    #Create an empty dictionary to create tree    
    if tree is None:                    
        tree={}
        tree[node] = {}
    


    for value in attValue:
        
        subtable = get_subtable(df,node,value)
        clValue,counts = np.unique(subtable[Class],return_counts=True)                        
        
        if len(counts)==1:#Checking purity of subset
            tree[node][value] = clValue[0]                                                    
        else:        
            tree[node][value] = buildTree(subtable) #Calling the function recursively 
                   
    return tree
  
  


# In[3]:


#from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer, StandardScaler
import pandas as pd
import numpy as np
data = pd.read_csv("F:\MLWS\\UHD\ML0607shibal.csv", encoding="utf-8", dtype=str, keep_default_na=False)


# In[4]:


eps=np.finfo(float).eps
from numpy import log2 as log


# In[5]:


df_train, df_test=train_test_split(data, test_size=0.4, random_state=29)
data


# In[6]:


t=buildTree(data)


# In[7]:


def predict (df, example):
    b = None
    #according to the decision tree
    #print(example[1])
    b='YES'
    NO = "C:\\Windows\\System32\\notepad.exe"
    if str(example[0]) == '(env_ERROR)':
        print("ERR")
        b="NO"
        
    elif example[0] == 'FALSE':
        print("FALSE")
        b="NO"
       
    else:
        if example[2] == 'pptx':
            print("PPT")
            b="NO"
            
        elif example[2] == 'pdf':
            print("PDF")
            b="NO"
            
            
        elif example[17] == NO:
            print("NOTEPAD")
            b="NO"
            
    
    #write testing results to dataset
    correct=0
    TP = 0
    FP = 0
    TN=0
    FN=0
    precesion = 0
    if example[-1]==b:
        correct = correct+1
    if example[-1]=='YES':
        if b =='YES':
            print("TP")
            TP= TP+1
        elif b=='NO':
            print("FP")
            FP = FP + 1
    else :
        if b=="YES" :
            print("FN")
            FN=FN+1
        else:
            print("TN")
            TN= TN+1
    example.append(b)
    #datasetFile.write(','.join(example))
    return b, correct, TP, FP,TN,FN


# In[8]:


decisionTree = buildTree(df_train)

#Test Cases
testset = df_test


# In[9]:


#datasetFile.seek(387,0)
tmp = 0
correct =0
TP=0
FP=0
TN=0
FN=0
for i in range(len(df_test)):
    result=predict(data, list(df_test.iloc[i]))
    ans = result[0]
    correct = correct +  result[1]
    print("Test case ",i,":",ans,"\n")
    tmp = tmp +1
    TP = result[2] + TP
    FP = result[3] + FP
    TN=result[4]+TN
    FN=result[5]+FN
print("====================PRECESION====================\n")
print("TN : ", TN)
print("FN : ", FN)
print("TP : ", TP)
print("FP : ", FP)
print("Classification Precesion : ", TP/(TP+FP))
print("\n==================ACCURACY======================\n")
print("try : ", tmp)
print("matched : ", correct)
print("Classification Accuracy : ", correct/tmp)


# In[10]:


import pprint
pprint.pprint(t)
pprint.pprint(decisionTree)


print(type(t))

import json

save_path="F:\git_workspace\\MLing\\result.json"
with open (save_path, 'w', encoding='utf-8') as json_f:
    json.dump(t, json_f, indent="\t")

