#In this program, we calculate the entropy weight of the 
# three-level indicators according to the  three-level indicator
#  data of personnel, technology and process respectively.
import numpy as np
import pandas as pd
fp="d:/P1.xlsx"
data=pd.read_excel(fp,index_col=None,header=None)
data = (data - data.min())/(data.max() - data.min())
m,n=data.shape
k=1/np.log(m)
yij=data.sum(axis=0)
pij=data/yij
#The second step, calculate pij
test=pij*np.log(pij)
test=np.nan_to_num(test)
ej=-k*(test.sum(axis=0))
#Calculate the information entropy of each indicator
wi=(1-ej)/np.sum(1-ej)
print(wi)