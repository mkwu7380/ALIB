import matplotlib
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv('/Users/macbookpro/github/ALIB/cardata.data')

encode = preprocessing.LabelEncoder()
buying = encode.fit_transform(list(data["buying"]))
maint = encode.fit_transform(list(data["maint"]))
door = encode.fit_transform(list(data["door"]))
persons = encode.fit_transform(list(data["persons"]))
lug_boot = encode.fit_transform(list(data["lug_boot"]))
safety = encode.fit_transform(list(data["safety"]))
cls = encode.fit_transform(list(data["class"]))

predict = "class"

x = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

print(x_train, y_test)
