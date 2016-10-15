import numpy
import netCDF4
import matplotlib.pyplot

GlobRunoff=netCDF4.Dataset('PCRGLOB-WB1979-2012Runoff.nc', 'r')
#reads all PCRGLOB-WB data
print (GlobRunoff)
VariableRunoff=GlobRunoff.variables['Runoff']
TestRunoff=VariableRunoff[100, 100]
print (TestRunoff)
image=matplotlib.pyplot.imshow(TestRunoff)
matplotlib.pyplot.show()

