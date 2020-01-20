"""
January 19th 2020
            Author T.Mizumoto
"""

#! python 3
# ver.x1.00
# SuperFigure.py  -  this program make a figure that be drown calculated the area and mesured point.

from stl import mesh
import numpy as np
import matplotlib.pyplot as plt
from rectselect import RectSelect

class SuperFigure(object):
    stl_path = ""
    # index-0: x-axis, index-1: y-axis
    PlotPoint = np.empty((0, 2))
    PlotData = np.empty((0,0))
    # cut_axis: x=0, y=1, z=2
    cut_axis = 2
    cut_point = 0.0
    # x=0, y=1, z=2
    plot_Xaxis = 0
    plot_Yaxis = 1
    # calculation area
    X_area = []
    Y_area = []

    def read_stl(self):
        stl_data = mesh.Mesh.from_file(self.stl_path)
        stl_2d = stl_data.vectors.reshape(-1, 3)
        # return Cross Section(CS) index
        index_CS = np.where(stl_2d[:, self.cut_axis] == self.cut_point)
        CS = np.empty((0, 3))
        for i in index_CS[0]:
            CS_1d = stl_2d[i, :]
            CS = np.append(CS, np.reshape(CS_1d, (1, 3)), axis = 0)
        self.CrossSection = CS
    
    def show(self):    
        fig1 = plt.figure(1)
        ax1 = fig1.add_subplot(111)
        ax1.plot(self.CrossSection[:, self.plot_Xaxis], self.CrossSection[:, self.plot_Yaxis], \
            color = "black", label = "object")
        ax1.set_xlim(self.X_area[0], self.X_area[1])
        ax1.set_ylim(self.Y_area[0], self.Y_area[1])
        region = RectSelect()
        region.plot = self.PlotPoint
        region.data = self.PlotData
        ax1.plot(region.plot[:, 0], region.plot[:, 1], ".", label = "plot")
        ax1.legend()
        ax1.grid()
        plt.show()
    


if __name__ == "__main__":
    from FFB_HISTORY import HISTORY
    hs = HISTORY()
    hs.path = "HISTORY/u-velociy/4C/rf_wake_4C.txt"
    hs.read()
    hs.coordinate()
    hs.measure_data()
    hs.separate_linenum(21)
    line = hs.line["line1"]

    SF = SuperFigure()
    SF.stl_path = "stl/Re4E5_STL.stl"
    SF.X_area = [-2, 7]
    SF.Y_area = [-3, 3]
    SF.read_stl()
    SF.PlotPoint = line[:, :2]
    SF.PlotData = line[:, 3:]
    SF.show()        