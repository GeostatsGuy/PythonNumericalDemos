import csv, sys
import os
import numpy as np
import pandas as pd
from scipy import misc

# Michael Pyrcz, Univ. of Texas at Austin, @GeostatsGuy
#
# Python Script to convert a JPG to intensity GSLIB File 
# python filter.py input_filename output_filename
#
# Example:
#
# python image2GSLIB my_image_file.jpg my_GSLIB_file.dat
#
def Dataframe2GSLIB(data_file,df):
    colArray = []
    colArray = df.columns
    ncol = len(df.columns) 
    nrow = len(df.index)
    file_out = open(data_file, "w")
    file_out.write(data_file + '\n')  
    file_out.write(str(ncol) + '\n') 
    for icol in range(0, ncol): 
        file_out.write(df.columns[icol]  + '\n')  
    
    for irow in range(0, nrow):
        for icol in range(0, ncol):
            file_out.write(str(df.iloc[irow,icol])+ ' ')  
        file_out.write('\n')

    file_out.close()    
  
filename = sys.argv[1]
outname = sys.argv[2]

arr = misc.imread(filename)

nx = arr.shape[0]
ny = arr.shape[1]

arr2 = np.zeros((nx*ny,4))

count = 0

for ix in range(0, nx): 
    for iy in range(0, ny):
        iix = int(nx-1) - int(ix) 
        arr2[count,0] = int(255) - (int(arr[iix,iy,0]) + int(arr[iix,iy,1]) + int(arr[iix,iy,2]))/3
        arr2[count,1] = (int(arr[ix,iy,0])) 
        arr2[count,2] = (int(arr[ix,iy,1])) 
        arr2[count,3] = (int(arr[ix,iy,2]))         
        count = count + 1

df = pd.DataFrame(arr2)
colArray = []
colArray.append("Intensity")
colArray.append("Red")
colArray.append("Green")
colArray.append("Blue")
df.columns = colArray

print("Written file is " + str(ny) + " by " + str(nx) + " - v1.2")

Dataframe2GSLIB(outname,df)