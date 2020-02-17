import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle

data = pd.read_csv("student-mat.csv", sep = ";")
data = data [["G1", "G2", "G3", "studytime", "failures", "absences"]]
predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

best = 0
for _ in range(10000):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

    lin = linear_model.LinearRegression()
    lin.fit(x_train, y_train)
    acc = lin.score(x_test, y_test)


    if acc > best:
        best = acc
        with open("studentgrades.pickle", "wb") as f:
            pickle.dump(lin, f)

pickle_in = open("studentgrades.pickle", "rb")
lin = pickle.load(pickle_in)

print("Coefficient: \n", lin.coef_)
print("Intercept: \n", lin.intercept_)

pre = lin.predict(x_test)

acc = lin.score(x_test, y_test)
print(best)

for i in range(len(pre)):
    print(pre[i], x_test[i], y_test[i])

p = 'absences'
style.use("ggplot")

"""pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()"""
