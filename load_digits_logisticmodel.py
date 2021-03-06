# -*- coding: utf-8 -*-
"""load_digits_logisticmodel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/161RmMquORYHbddHYWOZWQxqng06165iu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import load_digits
df=load_digits()

df.keys()

digits=df.data
labels=df.target

plt.figure(figsize=[10,10])
for i in range (1,6):
  s=np.random.randint(0,digits.shape[0]+1)
  x=digits[s]
  x=np.reshape(x,(8,8))
  y=labels
  plt.subplot(1,5,i)
  plt.imshow(x,cmap="gray")
  plt.title(f"digit: {y[s]}")

y=df.target

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")
model=LogisticRegression(max_iter=20,verbose=True)

x_train,x_test,y_train,y_test= train_test_split(digits,labels,test_size=0.2,random_state=5)

model.fit(x_train,y_train)

prediction=model.predict(x_test)

accuracy_score(y_test,prediction)

plt.figure(figsize=[10,10])
for i in range (1,6):
  s=np.random.randint(0,x_test.shape[0]+1)
  x=x_test[s]
  x=np.reshape(x,(8,8))
  y=prediction
  plt.subplot(1,5,i)
  plt.imshow(x,cmap="gray")
  plt.title(f"digit: {y[s]}")

