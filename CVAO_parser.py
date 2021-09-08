# CVAO_parser_v2.0
# python 3
# suit of functions to read in config, and meta files and to control the work flow
#
# b.brooks 08/2021

def read_meta(logfile, name):
   import pandas as pd
   import numpy as np
   from datetime import datetime
   import CVAO_common as com
   
   # read in meta
   try:
      df = pd.read_excel("meta.xlsx")
   except:
      # exit if problem encountered
      print("Unable to open meta.xlsx. This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Unable to open meta.xlsx. Program will terminate.\n')
      g.close()
      exit()     
      
   # find the approprate line
   inst = df.loc[:, 'instrument\n':'instrument\n':1].values
   tp = df.columns
   
   header = np.array(tp[1:len(tp)])      
   for x in range (0, len(inst)):
      if (name in inst[x]):
         tp = df.loc[x,:].values  
         dd = np.array(tp[1:len(tp)])
         break
            
   meta = np.empty([len(header), 2], dtype=object)       
  
   if 'dd' not in locals():
      print("Can't find meta data about named instrument. This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Can\'t find meta data about named instrument. Program will terminate.\n')
      g.close()
      exit()
   else:
      for x in range (0, len(header)):
         meta[x, 0] = header[x]
         meta[x, 1] = dd[x]
   
   del pd, datetime, np   
   
   return meta

def read_config(logfile):
   from datetime import datetime
   import time
   import calendar   
   import numpy as np
   
   # read in Config file
   try:
      f = open("Config.txt", "r")
      if f.mode == 'r':
         lines = f.readlines()
         f.close()
   except:
      # exit if problem encountered
      print("Unable to open Config.txt file. This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Unable to open Config.txt. Program will terminate.\n')
      g.close()
      exit()
      
   config = np.empty([7, 1], dtype=object)
   # process information in config file
   ss1 = "##### Start - do not remove #####"
   for x in range (0, len(lines)):
      if (ss1 in lines[x]):
         try:
            config[0] = str(lines[x+1].strip('\n')).strip('[]') #file version
            config[1] = str(lines[x+2].strip('\n')) # desired duration in file
            config[2] = str(lines[x+3].strip('\n')) # start date all or d, m, y
            config[3] = str(lines[x+4].strip('\n')) # instrument name
            config[4] = str(lines[x+5].strip('\n')) # data product
            config[5] = str(lines[x+6].strip('\n')) # path to data  
            config[6] = str(lines[x+7].strip('\n')) # standard version          
            break  
         except:   
            print("Error in. This program will terminate.")
            g = open(logfile, 'a')
            g.write(datetime.utcnow().isoformat() + ' Error in config file. Program will terminate.\n')
            g.close()
            exit()
      
   del lines, datetime, np, time, calendar
   
   return config

def do_run(config, meta, data, logfile):
   import CVAO_data as dat
   import CVAO_products as prod
   
   data.lat = 16.848
   data.lon = -24.871
   opt = ''
   
   if (config[3] == 'ncas-dc-gc-fid-4') and (config[4] == 'voc-concentration'):
      data = dat.ncas_dc_gc_fid_4(config, data, logfile) # this gets all the data in the file   
      data = dat.data_chunker(config, data, logfile) # this returns a data structure split into appropraite chuncks 
      
      try:
         for n in range(len(data.st)):
            data.counter = n # keeps track of where you are in the list (-1)
            nc = prod.create_NC_file(config, data.ET[data.st[n]], opt, logfile)
            #prod.voc_concentration(meta, data, nc)
            nc.close() 
      except:
         nc = prod.create_NC_file(config, data.ET[data.st], opt, logfile)
         prod.voc_concentration(meta, data, nc) # counter will be -1
         nc.close()
      exit()
   del dat, prod

def t_control(logfile): 
   from collections import namedtuple  
   
   # read in and process config file 
   config = read_config(logfile)
   
   # read in meta file
   meta = read_meta(logfile, config[3])
   
   #set up data tuple
   data = namedtuple("data", "") 
   
   # do the run
   do_run(config, meta, data, logfile)
   