"""
January 15th 2020
            Author T.Mizumoto
"""
#! python 3
# ver.1.00
# fun_ConvertFilename.py  -  this program convert to target name from basename.

import os

def fun_basename(path):
    basename = os.path.basename(path)
    basename = basename.rstrip(".txt")
    directoryname = os.path.split(path)[0] + "/"
    return basename, directoryname

# paht is base file path
def fun_CF_M(path):
    basename = os.path.basename(path)
    basename = basename.rstrip(".txt")
    directoryname = os.path.split(path)[0] + "/"
    M_path = directoryname + basename + "_MeasureData.txt"
    return basename, M_path, directoryname
    
def fun_CF_C(path):
    basename = os.path.basename(path)
    basename = basename.rstrip(".txt")
    directoryname = os.path.split(path)[0] + "/"
    C_path = directoryname + basename + "_Coordinate.txt"
    return basename, C_path, directoryname
    
def fun_CF_withParam(path):
    basename = os.path.basename(path)
    basename = basename.rstrip(".txt")
    directoryname = os.path.split(path)[0] + "/"
    WP_path = directoryname + basename + "_withDefParam.txt"
    return basename, WP_path, directoryname
    
def fun_CF_DefParamList(path):
    basename = os.path.basename(path)
    basename = basename.rstrip(".txt")
    directoryname = os.path.split(path)[0] + "/"
    PL_path = directoryname + basename + "_DefParamList.txt"
    return basename, PL_path, directoryname