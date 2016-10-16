import numpy as np
import netCDF4
import matplotlib.pyplot

GlobRunoff=netCDF4.Dataset('PCRGLOB-WB1979-2012Runoff.nc', 'r')
#reads all PCRGLOB-WB data
print (GlobRunoff)
latbounds=[ 40 , 43 ]
lonbounds=[ -96 , -89 ]
lats=GlobRunoff.variables['lat'][:]
lons=GlobRunoff.variables['lon'][:]
#latitude and longitude closest to bounds is found by
latli=np.argmin( np.abs( lats - latbounds[0]))
latui=np.argmin( np.abs( lats - latbounds[1]))
lonli=np.argmin( np.abs( lons - lonbounds[0]))
lonui=np.argmin( np.abs( lons - lonbounds[1]))
#subset
VariableRunoffsubset=GlobRunoff.variables['Runoff'][ 1 , latli:latui , lonli:lonui ]
print (VariableRunoffsubset)
image=matplotlib.pyplot.imshow(VariableRunoffsubset)
matplotlib.pyplot.title("Runoff for a catchment")
matplotlib.pyplot.colorbar()
matplotlib.pyplot.show()

