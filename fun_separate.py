"""
January 15th 2020
            Author T.Mizumoto
"""
#! python 3
# ver.1.00
# fun_separete.py  -  this program separete some data by coordinate base.

import numpy as np
import os
from fun_ConvertFilename import fun_CF_M, fun_CF_C

# point: 1 1 1 | 0 0 0 --> 3  starting line num is 1
def fun_separate_wake(path, point, wake1, wake2):
    basename, data_path, directoryname = fun_CF_M(path)
    basename, coor_path, directoryname = fun_CF_C(path)

    print("Data File Now Loading...")
    data = np.loadtxt(data_path)
    print("Coordinate File Now Loading...")
    coor = np.loadtxt(coor_path)

    data1 = data[:point]
    data2 = data[point:]
    coor1 = coor[:point]
    coor2 = coor[point:]

    np.savetxt(directoryname + "Sp_wake" + str(wake1) + "C_MeasureData.txt", data1)
    np.savetxt(directoryname + "Sp_wake" + str(wake2) + "C_MeasureData.txt", data2)
    np.savetxt(directoryname + "Sp_wake" + str(wake1) + "C_Coordinate.txt", coor1)
    np.savetxt(directoryname + "Sp_wake" + str(wake2) + "C_Coordinate.txt", coor2)
    print("Successful " + basename)

if __name__ == "__main__":
    from Gui import FilePath
    fp = FilePath()
    fp.path("txt")
    filepath = fp.filepath_list
    if filepath == [""]:
        print("File Path Not Selected.")
    else:
        point_list = [1120, 1120]
        wake_list = [["3-1", "4-1"], ["3-2", "4-2"]]
        for i in range(len(filepath)):
           fun_separate_wake(filepath[i], point_list[i], wake_list[i][0], wake_list[i][1])

