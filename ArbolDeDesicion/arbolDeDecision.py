import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

data = pd.read_csv("wine.csv", sep=",")
data.head()

data.shape

data.describe()

plt.hist(data)

predictors_col = ["1", "14.23", "2.43", "15.6", "127", "2.8", "3.06", ".28", "2.29", "5.64", "1.04","3.92"]
target_col = ["1065"]

predictors = data[predictors_col]
target = data[target_col]

x_train, x_test, y_train, y_test = train_test_split(predictors, target, test_size=0.25, random_state=13)
tree = DecisionTreeClassifier()
arbol = tree.fit(x_train, y_train)
plot_tree(arboarboll)

