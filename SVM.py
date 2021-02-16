# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:29:57 2021

@author: gggg8
"""


from __future__ import absolute_import, division, print_function, unicode_literals
try:
  # %tensorflow_version only exists in Colab.
  %tensorflow_version 2.x
except Exception:
  pass
import numpy as np
import pandas as pd
import tensorflow as tf
import os
import matplotlib.pyplot as plt

data = pd.read_csv('F:\MLWS\index4train.csv', encoding='utf-8')

data[:5]

from sklearn.model_selection import train_test_split

print(data)

TF=data.pop('TF')
print(data)
print(TF)

X_train, X_test, y_train, y_test = train_test_split(data, TF, test_size = 0.3)

print(y_train)
print(X_train)
print(X_test)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train_std = X_train.to_numpy()
X_test_std = X_test.to_numpy()
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

print(X_test.shape)
print(X_train_std.shape)
print(y_test.shape)
print(y_train.shape)

from sklearn.svm import SVC
#from sklearn.svm import LinearSVC
#svm_model = LinearSVC(C=1)
svm_model = SVC(kernel='rbf', C=8, gamma=0.1)
print(X_train)
print(X_train_std)

svm_model.fit(X_train_std, y_train)
score = svm_model.score(X_train_std, y_train)
print(score)

y_pred = svm_model.predict(X_test_std)

print(X_train,",",y_train)
print(X_test,",",y_test)


print("예측된 라벨:", y_pred)
print("ground-truth 라벨:", y_test)

print("prediction accuracy: {:.9f}".format(np.mean(y_pred == y_test)))


y_train.value_counts().plot(kind='bar');
y_test.value_counts().plot(kind='bar');
X_test.value_counts().plot(kind='bar');
X_train.value_counts().plot(kind='bar');


X_train_std.shape, X_test.shape, y_train.shape, y_test.shape


from sklearn.svm import LinearSVC
from mpl_toolkits.mplot3d import Axes3D, axes3d
import mglearn
lin_svm_model=LinearSVC().fit(X_train_std, y_train)
coef, intercept=lin_svm_model.coef_.ravel(),lin_svm_model.intercept_

figure=plt.figure()

#ax=Axes3D(figure, elev=-152, azim=-26)
ax=figure.add_subplot(111,projection='3d')

xx = np.linspace(X_train_std[:, 0].min() - 2, X_train_std[:, 0].max() + 2, 50)
yy = np.linspace(X_train_std[:, 1].min() - 2, X_train_std[:, 1].max() + 2, 50)
mask=y_train==1
XX, YY = np.meshgrid(xx, yy)
ZZ = (coef[0] * XX + coef[1] * YY + intercept) / -coef[2]
ax.plot_surface(XX, YY, ZZ, rstride=16, cstride=16, alpha=0.3)
ax.scatter(X_train_std[mask, 0], X_train_std[mask, 1], X_train_std[mask, 2], c='b',
           cmap=mglearn.cm2, s=60, edgecolor='k')
ax.scatter(X_train_std[~mask, 0], X_train_std[~mask, 1], X_train_std[~mask, 2], c='r', marker='^',
           cmap=mglearn.cm2, s=60, edgecolor='k')

ax.set_xlabel("특성0")
ax.set_ylabel("특성1")
ax.set_zlabel("특성1 ** 2")
'''
scale = 300
xmax = X_train_std[:,0].max()+1
xmin = X_train_std[:,0].min()-1
ymax = X_train_std[:,1].max()+1
ymin = X_train_std[:,1].min()-1


xx = np.linspace(xmin,xmax,scale)
yy = np.linspace(ymin,ymax,scale)
data1, data2 = np.meshgrid(xx,yy)
X_grid = np.c_[data1.ravel(), data2.ravel()]
pred_y = svm_model.predict(X_grid)

fig=plt.figure(figsize=[12,10])

CS = plt.imshow(pred_y.reshape(scale,scale), interpolation=None, origin='lower',
                extent=[xmin,xmax,ymin,ymax], alpha=0.3, cmap='gray_r')

# draw X_train
plt.scatter(X_train_std[:,0], X_train_std[:,1], c=y_train, s=60)

plt.xlabel(iris.feature_names[col1])
plt.ylabel(iris.feature_names[col2])
plt.colorbar(CS, shrink=0.3)
plt.title('Linear SVC - Iris',fontsize=20)'''



X=X_test_std
y=y_test
ZZ=X*y

plt.figure()
print("KJ")
plt.contour(ZZ)
print("KJJ")
plt.show()
print("KJUI")

dec = lin_svm_model.decision_function(np.c_[XX.ravel(), YY.ravel(), ZZ.ravel()])
plt.contourf(XX, YY, dec.reshape(XX.shape), levels=[dec.min(), 0, dec.max()],
             cmap=mglearn.cm2, alpha=0.5)
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.xlabel("x_tst_std0")
plt.ylabel("y_tst 1")