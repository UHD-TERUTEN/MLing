# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 22:27:51 2021

@author: gggg8
"""

import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import numpy as np
data = pd.read_csv('F:\MLWS\index4train.csv', encoding='utf-8')

data.head()

samples=data

print(data)

processed_data=data.copy()
#label=data.pop('FiN')
#name=data.pop('PN')


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

print(sc.fit(data))

std_data=sc.transform(data)

print(std_data)

std_label=std_data[0]
std_name=std_data[9]

#processed_data[['FiN', 'PN']] = sc.fit_transform(processed_data[['FiN', 'PN']])

print("STD")
print(std_label)
print(std_name)

print(data)
plt.scatter(std_label,std_name)
plt.show()
# K 값을 늘려가며 반복 테스트
for i in range (1, 14):
       # 클러스터 생성
       estimator = KMeans(n_clusters = i)
       ids = estimator.fit_predict(processed_data[['FiN', 'PN']])

       # 2행 3열을 가진 서브플롯 추가 (인덱스 = i)
       plt.tight_layout()

        # 서브플롯의 라벨링
       plt.xlabel('FileName')
       plt.ylabel('ProgramName')
        # 클러스터링 그리기
       plt.scatter(processed_data['FiN'], processed_data['PN'], c=ids)
       plt.show()
plt.show()




