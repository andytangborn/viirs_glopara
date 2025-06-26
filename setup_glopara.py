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




path_in = '/scratch1/NCEPDEV/global/glopara/dump/'
path_out = '/scratch1/NCEPDEV/da/Andrew.Tangborn/GEFS-Aero/glopara_dump/'

year = 2021
month = 7 
day_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31] 
hour_list = [0, 6, 12, 18]
for day in day_list:
  glopara_path_out_day = path_out + 'gdas.' + str(year)+str(month).zfill(2)+str(day).zfill(2)
  day_file = Path(glopara_path_out_day) 
  isExist = os.path.exists(day_file)
  if not isExist:
    os.makedirs(day_file)
  for hour in hour_list:
    glopara_path_out = path_out + 'gdas.' + str(year)+str(month).zfill(2)+str(day).zfill(2)+'/'+str(hour).zfill(2)+'/atmos/' 
    glopara_path_in = path_in + 'gdas.' + str(year)+str(month).zfill(2)+str(day).zfill(2)+'/'+str(hour).zfill(2)+'/atmos/'
    hour_file = Path(glopara_path_out)
    isExist = os.path.exists(hour_file)
    if not isExist:
      os.makedirs(hour_file)
    os.chdir(hour_file)
    print('current directory = ',glopara_path_out) 
    print('target directory = ',glopara_path_in)
    for item in os.listdir(glopara_path_in):
      print('item = ',item)
      src_path = os.path.join(glopara_path_in, item)
      dest_path = os.path.join(glopara_path_out, item)
      if os.path.isfile(src_path):
        print('src_path = ', src_path)
        print('dest_path = ', dest_path)
        os.symlink(src_path, dest_path)
      elif os.path.isdir(src_path):
        os.symlink(src_path, dest_path, target_is_directory=True)
