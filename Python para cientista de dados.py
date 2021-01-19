# import pandas as pd
# import numpy as np
#
# base = pd.read_csv(r"C:\Users\paulo.roberto\Documents\Python\Formação Cientista de Dados com Python e R\Dados\iris.csv")
#
# amostra = np.random.choice(a = [0, 1], size=150, replace= True, p = [0.5, 0.5])
# print(amostra)

import os
import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
#
os.chdir(r"C:\Users\paulo.roberto\Documents\Python\Formação Cientista de Dados com Python e R\Dados")
#
# iris = pd.read_csv("iris.csv")
# iris['class'].value_counts()
#
# x, _, y,_ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size = 0.5, stratify = iris.iloc[:, 4])
#
# infert = pd.read_csv('infert.csv')
# x1, _, y1, _ =
from math import ceil
população = 150
amostra = 15
k = ceil(população / amostra)
r = np.random.randint(low=1, high=k+1, size=1)
acumulador = r[0]
sorteados = []

for i in range(amostra):
    sorteados.append(acumulador)
    acumulador += k

base = pd.read_csv('iris.csv')
basefinal = base.loc[sorteados]
print(basefinal)