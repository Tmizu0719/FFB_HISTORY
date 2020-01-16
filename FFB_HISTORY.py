"""
January 12th 2020
            Author T.Mizumoto
"""
#! python 3
# ver.1.10
# FFB_HISTORY.py  -  this program exrtact coordinate and calculate data.

import numpy as np
import re

class HISTORY:
    path = ""
    data_num = 0
    coordinate_num = 0
    param_list = []
    data_list = []
    coordinate_list = []
    default_param = 28

    # txt file ---> param_list(coordinate etc.), data_list(numpy.array) 
    def read(self):
        with open(self.path) as f:
            txt_list = [i.strip() for i in f.readlines()]
        
        param_list = []
        strdata_list = []
        for i in txt_list:
            if i[0] == "#":
                param_list.append(i)
            else:
                strdata_list.append(i)
        self.param_list = param_list
        
        data_list = []
        for i in strdata_list:
            """
            sprit_strdata = i.split("  ")
            oneS_data = sprit_strdata[4].split(" ")
            sprit_strdata[4] = oneS_data[0]
            sprit_strdata[5] = oneS_data[1]
            """
            sprit_strdata = re.findall(r"\d\.\d+E\S\d+|\S\d\.\d+E\S\d+", i)
            data_line = [float(j) for j in sprit_strdata]
            data_list.append(data_line)
        self.data_list = np.array(data_list)
        self.data_num = len(data_list)
        
    
    # extract coordinate
    def coordinate(self):
        coordinate_list = []
        for i in self.param_list:
            jugde = re.search(r";", i)
            if jugde == None:
                pass
            else:
                coordinate = re.findall(r"\d\.\d+", i)
                if coordinate == []:
                    coordinate = [float("nan"), float("nan"), float("nan")]
                else:
                    coordinate = [float(j) for j in coordinate]
                coordinate_list.append(coordinate)
        self.default_param = len(self.param_list) - len(coordinate_list) - 5
        self.coordinate_list = np.array(coordinate_list)
        self.coordinate_num = len(coordinate_list)

    def measure_data(self):
        self.measure_data = self.data_list[:, self.default_param:]
        self.param_data = self.data_list[:, :self.default_param]

    def savetxt(self, folder, name):
        np.savetxt(folder + name + "_DefParamData.txt", self.param_data)
        np.savetxt(folder + name + "_MeasureData.txt", self.measure_data)
        np.savetxt(folder + name + "_Coordinate.txt", self.coordinate_list)
        with open(folder + name + "_DefParamList.txt", mode = "w") as f:
            f.writelines(self.param_list)

    def savecsv(self, folder, name):
        np.savetxt(folder + name + "_DefParamData.csv", self.param_data, delimiter = ",")
        np.savetxt(folder + name + "_MeasureData.csv", self.measure_data, delimiter = ",")
        np.savetxt(folder + name + "_Coordinate.csv", self.coordinate_list, delimiter = ",")
        with open(folder + name + "_DefParamList.txt", mode = "w") as f:
            f.writelines(self.param_list)


if __name__ == "__main__":
    # get filepath
    from Gui import FilePath
    fp = FilePath()
    fp.path("txt")
    filepath = fp.filepath_list
    if filepath == [""]:
        print("File Path Not Selected.")
    else:
        import os
        from fun_ConvertFilename import fun_basename
        for i in filepath:
            hs = HISTORY()
            hs.path = i
            basename, directoryname = fun_basename(i)
            print(basename + " now loading...")
            hs.read()
            hs.coordinate()
            hs.measure_data()
            hs.savetxt(directoryname, basename)
            print("Successful " + basename)