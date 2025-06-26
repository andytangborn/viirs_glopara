import numpy as np
import os
import math
import subprocess as sp
from pathlib import Path
#import matplotlib.pyplot as plt
#from emcpy.plots import CreateMap
#from emcpy.plots.map_tools import Domain, MapProjection
#from emcpy.plots.map_plots import MapGridded
import netCDF4 as nc
import glob
import array
import time
import shutil 




path_in = '/scratch2/NCEPDEV/stmp3/Andrew.Tangborn/VIIRS/thin0.9999/'
path_out = '/scratch1/NCEPDEV/stmp2/Andrew.Tangborn/GEFS-Aero/glopara_dump/'

year = 2021
month = 4 
day_list = [12,13,14,15,16,17,18,19,20,21,22,23]
hour_list = [0, 6, 12, 18]
for day in day_list:
  
  for hour in hour_list:
    file_n20 = 'gdas.t'+str(hour).zfill(2)+'z.viirs_n20.'+str(year)+str(month).zfill(2)+str(day).zfill(2)+str(hour).zfill(2)+'.nc4'
    file_npp = 'gdas.t'+str(hour).zfill(2)+'z.viirs_npp.'+str(year)+str(month).zfill(2)+str(day).zfill(2)+str(hour).zfill(2)+'.nc4'
    n20_file = path_in+str(year)+str(month).zfill(2)+str(day).zfill(2)+'/'+file_n20
    npp_file = path_in+str(year)+str(month).zfill(2)+str(day).zfill(2)+'/'+file_npp 
    file_out_n20 = path_out+'gdas.'+str(year)+str(month).zfill(2)+str(day).zfill(2)+'/'+str(hour).zfill(2)+'/atmos/'+file_n20
    file_out_npp = path_out+'gdas.'+str(year)+str(month).zfill(2)+str(day).zfill(2)+'/'+str(hour).zfill(2)+'/atmos/'+file_npp
    shutil.copy(n20_file,file_out_n20)
    shutil.copy(npp_file,file_out_npp)
    
    print('npp_file = ',npp_file) 
  
