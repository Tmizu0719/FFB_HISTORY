"""
January 20th 2020
            Author T.Mizumoto
"""

#! python 3
# ver.x1.00
# rectselect.py  -  this program select some plot point and draw data at select points

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.widgets import RectangleSelector

class RectSelect(object):
    def __init__(self, ax=None):
        self.ax = ax or plt.gca()
        self.rect = Rectangle((0,0), 0, 0, color='orange', alpha=0.5)
        self.ax.add_patch(self.rect)
        self.blc = np.zeros(2)
        self.trc = np.zeros(2)
        self.plot = np.empty(2)
        self.data = np.empty(1)

        def selector(event):
            if event.key in ['Q', 'q'] and selector.RS.active:
                print ('RectSelect deactivated.')
                selector.RS.set_active(False)
            if event.key in ['A', 'a'] and not selector.RS.active:
                print ('RectSelect activated.')
                selector.RS.set_active(True)

        selector.RS = RectangleSelector(self.ax, self.callback)
        self.ax.figure.canvas.mpl_connect('key_press_event', selector)
        self.ax.figure.canvas.mpl_connect('button_release_event', self.release)

    def callback(self, eclick, erelease):
        x0, x1 = eclick.xdata, erelease.xdata
        y0, y1 = eclick.ydata, erelease.ydata
        self.blc = min(x0, x1), min(y0, y1)
        self.trc = max(x0, x1), max(y0, y1)
        blc_print = '({:0.4},{:0.4})'.format(*self.blc)
        trc_print = '({:0.4},{:0.4})'.format(*self.trc)
        print('blc={}, trc={}'.format(blc_print, trc_print))
        self.draw_figure()

    def release(self, event):
        self.rect.set_width(self.trc[0] - self.blc[0])
        self.rect.set_height(self.trc[1] - self.blc[1])
        self.rect.set_xy(self.blc)
        self.ax.figure.canvas.draw()

    def extract_point(self):
        # SP: Selected points
        index_SP = np.where((self.blc[0] <= self.plot[:, 0]) & (self.plot[:, 0] <= self.trc[0]) \
            & (self.blc[1] <= self.plot[:, 1]) & (self.plot[:, 1] <= self.trc[1]))
        SP = np.empty((0, 2))
        for i in index_SP[0]:
            SP_1d = self.plot[i, :]
            SP = np.append(SP, np.reshape(SP_1d, (1, 2)), axis = 0)
        print(SP)
        return index_SP, SP

    def draw_figure(self):
        index_SP, SP = self.extract_point()
        if len(index_SP[0]) == 0:
            pass
        else:
            # get data at plot points
            SP_data = np.empty((0, self.data.shape[0]))
            for i in index_SP[0]:
                SP_data_1d = self.data[:, i]
                SP_data = np.append(SP_data, np.reshape(SP_data_1d, (1, self.data.shape[0])), axis = 0)
            # mean data at plot points
            SP_data_mean = np.mean(SP_data, axis = 0)

            # draw a figure
            fig2 = plt.figure(2)
            ax2 = fig2.add_subplot(111)
            for i in range(SP_data.shape[0]):
                ax2.plot(range(self.data.shape[0]), SP_data[i, :], label = "No." + str(i))
            ax2.plot(range(self.data.shape[0]), SP_data_mean, label = "mean")
            fig2.legend()
            fig2.show()



if __name__ == "__main__":
    x = range(10)
    y = range(10)
    data = np.random.random(1000) * 10
    
    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(111)
    ax1.plot(x,y,'.')

    region = RectSelect()
    region.plot = np.stack((x, y), axis = 1)
    region.data = np.reshape(data, (-1, 10))
    
    plt.show()