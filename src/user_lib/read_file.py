#!/usr/bin/env python3
# 

import pandas as pd



def readDataFromXls(pathtofile,sheetname):
    # read data from xls-file
    df = pd.read_excel(pathtofile, sheet_name= sheetname,index_col=0)  
    df = df.reset_index()
    return df