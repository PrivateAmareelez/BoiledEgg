import os

import numpy as np
import statsmodels.api as sm

rawData = {}


def loadData():
    for file in os.listdir("./data"):
        if file.endswith(".txt"):
            f = open("data/" + file)
            for line in f.readlines():
                values = map(float, line.split("\t"))
                if rawData.has_key(values[0]):
                    rawData[values[0]].append(values[1])
                else:
                    rawData[values[0]] = [values[1]]


def prepareData(data):
    y = []
    x = []
    for key in data:
        if len(data[key]) == 4:
            y.append(key)
            x.append(data[key])
    return [y, np.column_stack((np.row_stack(x), np.ones(len(x))))]


loadData()
data = prepareData(rawData)

res = sm.OLS(data[0], data[1]).fit()
print res.summary()
