"""
January 13th 2020
            Author T.Mizumoto
"""

#! python 3
# ver.x1.00
# Integral-Scale_function.py  -  this program calculate integral-scale and correlation.

import numpy as np
from scipy.integrate import simps
from scipy.stats import pearsonr
import pandas as pd

# index_basepoint = 0 (defult)
def fun_CrossCorr(data, index_basepoint):
    alpha = data[:, index_basepoint]
    cross_corretion = []
    p_value = []
    matrix_num = data.shape
    point_num = int(matrix_num[1])
    for i in range(point_num):
        line = data[:, i]
        cc, p = pearsonr(alpha, line)
        cross_corretion.append(cc)
        p_value.append(p)
    df_CC = pd.DataFrame(columns = ["CrossCorrelation", "Pvalue"])
    df_CC["CrossCorrelation"] = cross_corretion
    df_CC["Pvalue"] = p_value
    return df_CC


def fun_IntegralScale(correlation, distance):
    # find the first negative point
    minus = np.where(correlation < 0)
    first_minus = minus[0][0]
    
    # extract positibe points
    corr_plus = list(correlation[:first_minus])
    dis_plus = distance[:first_minus]
    complement = (distance[first_minus + 1] - distance[first_minus]) / 2 + distance[first_minus]
    corr_plus.append(0.0)
    dis_plus.append(complement)

    # integrate
    integral = simps(corr_plus, dis_plus)
    return integral


if __name__ == "__main__":
    from graph import Graph
    import matplotlib.pyplot as plt

    # read data
    data_path = "HISTORY/z-traverse_2-1-0_MeasureData.txt"
    data = np.loadtxt(data_path)
    coord_path = "HISTORY/z-traverse_2-1-0_Coordinate.txt"
    coord = np.loadtxt(coord_path)
    point = [0, 161, 322, 483, 644, 805, 966, 1127, 1288, 1449]
    name = ["X2-MVD", "X2-RMS1", "X2-RMS2", "X1-MVD", "X1-RMS1", "X1-RMS2", "X0-MVD", "X0-RMS1", "X0-RMS2"]

    IS_list = []
    for i in range(9):
        pstart = point[i]
        pend = point[i + 1]
        # calculate CrossCorrelation
        df_CC = fun_CrossCorr(data[:, pstart:pend], 0)
        # only z-traverse
        z_axis = coord[pstart:pend, 2]
        distance = []
        for j in z_axis:
            diff = j - z_axis[0]
            distance.append(diff)

        IS = fun_IntegralScale(df_CC["CrossCorrelation"], distance)
        IS_list.append(IS)

        g = Graph()
        g.label = ["CrossCorrelation", "Pvalue"]
        g.line(distance, df_CC["CrossCorrelation"], 0)
        g.line(distance, df_CC["Pvalue"], 1)
        plt.legend(title = "IS = " + str(IS))
        g.save_graph("graph/Z-traverse/" + name[i])
    print(IS_list)