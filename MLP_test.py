import numpy as np
import pandas as pd

import urllib.request

import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/maskot1977/ipython_notebook/master/toydata/iris.txt"
urllib.request.urlretrieve(url, 'iris.txt') 

df = pd.read_csv("iris.txt", sep="\t", index_col=0)
print(df.shape) # 何行何列か確認する
df.head() # 先頭五行の内容を確認する

"""
X = np.array(df.iloc[:, :4].values) 
Y = np.array(df.iloc[:, 4])

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(max_iter=10000)

clf.fit(X, Y)
"""