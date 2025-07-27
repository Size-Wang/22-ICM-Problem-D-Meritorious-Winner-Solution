#In this program, we transform the excel-data to calcluatable data. Then, we
#use EMW algorithm to work out the value of secondary score.
#

import xlrd
import xlwt
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import sparse
from scipy.optimize import leastsq

def func(a,x):
    k,b = a
    return k*x + b

def dist(a,x,y):
    return func(a,x) - y

if __name__ == '__main__':
    exc = xlrd.open_workbook("Data_Extract_From_Education_Statistics4.xlsx")
    table = exc.sheet_by_index(0)
    nrows = table.nrows

    data = np.zeros([336,9])

    # l = []
    # for i in range(5,14):
    #     l += table.col_types(i)
    # s = set(l)
    # print(s)

    availbe_num = np.zeros([336])
    average0 = np.zeros([336])
    average1 = np.zeros([336])
    param = [0,0]
    for i in range(1,337):
        X = []
        Y = []
        for j in range(5,14):
            if table.cell_type(i,j)==2:
                data[i-1][j-5] = table.cell_value(i,j)
                availbe_num[i-1] += 1
                average1[i-1] += data[i-1][j-5]
                X.append(j-5)
                Y.append(data[i-1][j-5])
        if availbe_num[i-1]>=5:
            X = np.array(X)
            Y = np.array(Y)
            var = leastsq(dist,param,args=(X,Y))
            for j in range(9):
                if data[i-1][j]==0:
                    data[i-1][j] = func(var[0],j)
                    average1[i-1] += data[i-1][j]
            average1[i-1] /= 9
        else:
            if availbe_num[i-1]!=0:
                average1[i-1] = average1[i-1] / availbe_num[i-1]
            else:
                average1[i-1] = 0

    average0 = np.sum(data,axis=1)
    average0 = average0 / availbe_num

  #  print(average0)

    file = xlwt.Workbook(encoding="utf-8")
    wtSheet = file.add_sheet('adding_data',cell_overwrite_ok=True)
    for i in range(336):
        for j in range(9):
            wtSheet.write(i+1,j+5,data[i][j])

    wtSheet.write(0,14,"average")
    for i in range(336):
        wtSheet.write(i+1,14,average1[i])
    file.save("edited.xls")
    #print(table.row(0)[5:14])