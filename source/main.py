#-*- coding: utf-8 -*-
import h5py


def getDataFromH5py(fileName,target,start,length):
    h5f = h5py.File(fileName, 'r')
    list(h5f.keys())
    print(l)
    if not h5f.__contains__(target):
        res = []
    elif(start+length>=h5f[target].shape[0]):
        res = h5f[target].value[start:h5f[target].shape[0]]
    else:
        res = h5f[target].value[start:start+length]
    h5f.close()
    return res



def main():
    """项目主函数"""
    file_name = './34465A Data Log 2020-06-12 12-59-16 72.hdf5'
    h5 = h5py.File('../input_hdf5_data/Data_Log.hdf5', 'r')
    print(list(h5.keys()))
    h5.close()
main()
