import scipy.stats as ss
import numpy as np
import netCDF4
import matplotlib.pyplot
import os
import sys
import glob
import pandas as pd
import osgeo

#GlobRunoff=netCDF4.Dataset('PCRGLOB-WB1979-2012Runoff.nc', 'r')
#reads all PCRGLOB-WB data
#print (GlobRunoff)
latbounds=[ -40 , -10 ]
lonbounds=[ 110 , 155 ]
#lats=GlobRunoff.variables['lat'][:]
#lons=GlobRunoff.variables['lon'][:]
#latitude and longitude closest to bounds is found by
#latli=np.argmin( np.abs( lats - latbounds[0]))
#latui=np.argmin( np.abs( lats - latbounds[1]))
#lonli=np.argmin( np.abs( lons - lonbounds[0]))
#lonui=np.argmin( np.abs( lons - lonbounds[1]))
#subset
#VariableRunoffsubset=GlobRunoff.variables['Runoff'][ : , latli:latui , lonli:lonui ]
#print (VariableRunoffsubset)
#Loop multiple observation files
os.chdir('/home/nils/Australia/Observations/780_catchments')
#xlsx_file=pd.ExcelFile('318164.xlsx')
#xlsx_file.sheet_names
#df=xlsx_file.parse('318164')
#print(df)
all_Data=pd.DataFrame()
for WorkingFile in os.listdir('/home/nils/Australia/Observations/780_catchments'):
    df=pd.read_excel(WorkingFile)
    all_Data1=all_Data.append(df,ignore_index=True)
    print (all_Data)
    #os.chdir('/home/nils/Australia/Observations/780_catchments')   
    #xls_file=pd.ExcelFile(WorkingFile)
    #xls_file.sheet_names
    #df=xls_file.parse('')
    #df

#print(len(xlsx_file))
 
#image=matplotlib.pyplot.imshow(VariableRunoffsubset)
#matplotlib.pyplot.title("Runoff for a catchment")
#matplotlib.pyplot.colorbar()
#matplotlib.pyplot.show()
#Calculating runoff signatures
#percentilePCR=np.percentile(VariableRunoffsubset, 99)
#print (percentilePCR)

#normalized differences between sim and obs

