"""
January 15th 2020
            Author T.Mizumoto
"""

#! python 3
# ver.1.00
# Gui.py  -  this program is my module about GUI.


import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog


### get file path ###
# enter self.path(extension) --> return self.filepath_list
class FilePath():
    def path(self, extension):
        self.root = tk.Tk()
        self.root.title("select files")
        bt_file = tk.Button(self.root, text = "select file", command = lambda: self.get_filepath(extension), bg = "#bbbbff")
        self.file_path = tksc.ScrolledText(self.root, wrap = tk.WORD, height = 10, width = 70)
        bt_get = tk.Button(self.root, text = "get file path", command = lambda: self.end(), bg = "#ff6464")
        
        for i in [bt_file, self.file_path, bt_get]:
            i.pack()
        self.root.mainloop()

    def get_filepath(self, filetype):
        filetype_list = [(filetype + " file", "*." + filetype), ("all file", "*")]
        filepath = filedialog.askopenfilenames(filetype = filetype_list, title = "select file")
        filepath = list(filepath)
        self.file_path.insert(tk.END, filepath)

    def get_scrtxt(self, txtbox):
        self.filepath_list = []
        self.filepath_list.append(txtbox.get("1.0", "end -1c"))
        self.filepath_list = str(self.filepath_list[0]).split(" ")

    def end(self):
        self.get_scrtxt(self.file_path)
        self.root.destroy()


if __name__ == "__main__":
    gui = FilePath()
    gui.path("txt")
    print(gui.filepath_list)