import numpy as np
import pandas as pd

df = pd.read_csv('./dataset/train.csv')
X=df[['LotArea','OverallQual','OverallCond']].values
Y=df[['SalePrice']].values
Xt=np.transpose(X)
B=np.matmul(np.matmul(np.matrix(np.matmul(Xt,X)).I,Xt),Y)
B=np.concatenate(B)
# B=B.reshape(1,3)
print(B)