#In this program, we work out the final score of each country by calculating 
#the area of triangle formulated by three secondary score.

import numpy as np
import math
import xlrd
import xlwt

def EWM(data,country_num,variate_num):
    maxium = np.max(data, axis=0)
    minium = np.min(data, axis=0)
    data_norm = (data - minium) * 1.0 / (maxium - minium)
 #   print(data_norm)
    sumzb = np.sum(data, axis=0)
    a = data / sumzb
    # 对ln0处理
#    a = data_norm * 1.0
    a[np.where(data_norm == 0)] = 0.00000001
    #    #计算每个指标的熵
    e = (-1.0 / np.log(country_num)) * np.sum(a * np.log(a), axis=0)
    #print(e)
    #    #计算权重
    w = (1 - e) / np.sum(1 - e)
    recodes = np.sum(a * w, axis=1)
    # print(w)
    # print(recodes)
    return w,recodes

if __name__ == '__main__':
    exc = xlrd.open_workbook("nation.xlsx")
    names = exc.sheet_names()

    # writeFile = xlwt.Workbook(encoding="utf-8")
    scores = np.zeros([16,3])
    for i in range(3):
        table = exc.sheet_by_index(i)
        nrows = table.nrows
        ncols = table.ncols
        data = np.zeros([nrows,ncols])
        for j in range(ncols):
            col = table.col_values(j)
            nozs = np.count_nonzero(col)
            ave = sum(col)/nozs
            col = np.array(col)
            np.putmask(col,col==0,ave)
            data[:,j] = col
        #print(data)
        # print(names[i])
        w,score = EWM(data,14,ncols)
        # print("\n")
    #     wtSheet = writeFile.add_sheet(names[i])
    #     for j in range(nrows):
    #         wtSheet.write(j,1,score[j])
    #     for j in range(ncols):
    #         wtSheet.write(1,j+3,w[j])
    #
    # writeFile.save("secondScore.xls")

        scores[:,i] = score
    # D = np.zeros(16)
    D = np.sum(scores,axis=1)
    # for i in range(16):
        # for u in range(0,2):
        #     for v in range(u+1,3):
        #         D[i] += scores[i][u] * scores[i][v] * math.sqrt(3)/4
    print(D)

    nations_name = ["AUS","BRA","KHM","CMR","CAN","CHN","DEU","KOR","LBY",
    "MEX","NZL","NOR","PAK","CHE","GBR","USA"]
    result = []
    for i in range(16):
        result.append((nations_name[i],D[i]))
    result.sort(key=lambda x : x[1],reverse=True)
    print(result)
    # print(scores)
    # DI = np.sum(scores,axis=1)
    # ave = DI/3
    # S = np.zeros(16)
    # for i in range(16):
    #     for j in range(3):
    #         S[i] += (scores[i][j]-ave[i])**2
    # S = np.sqrt(S/3)
    # CI = 1 - S/ave
    # print(DI)
    # print(CI)
    #
    # F = 2*DI*CI/(DI + CI)
    # print(F)