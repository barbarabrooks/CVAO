def ncas_dc_gc_fid_4(config, data, logfile): 
   import pandas as pd
   import numpy as np
   import time
   import os
   from datetime import datetime
   import calendar   
   
   fn = os.path.normpath(str(config[5]).strip('[]'))
   fn = fn[1:len(fn)-1] 
   try:
      df = pd.read_csv(fn,'\t')
   except:
      # exit if problem encountered
      print("Unable to open data file: ", fn , ". This program will terminate")
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat() + ' Unable to open data file: ' + fn + 'Program will terminate.\n')
      g.close()
      exit()
    
   DT = []
   ET = []
   DoY = []
   
   header = df.columns
   #parse time
   ds = df.loc[:,header[0]:header[0]:1].values #extract date from data frame column 1
   
   for i in range(0, len(ds)):
      try: 
         tt = time.strptime(str(ds[i]), "['%d/%m/%Y %H:%M']")
      except:
         tt = time.strptime(str(ds[i]), "['%d/%m/%Y %H:%M:%S']")
      
      #DoY
      DoY.append(float(tt[7]) + ((((float(tt[5])/60) + float(tt[4]))/60) + float(tt[3]))/24) 
      #ET
      ET.append(int(calendar.timegm(tt)))
      #DT
      DT.append(tt[0:6])
   
   #remove any nans from data
   
   df[header[1]].fillna(-1.00e+20, inplace = True) 
   
   data.species1   = np.array(df.loc[:, header[1]:header[1]:1].values)
   data.flag1 = np.array(df.loc[:, header[2]:header[2]:1].values)
   data.species2 = np.array(df.loc[:, header[3]:header[3]:1].values)
   data.flag2 = np.array(df.loc[:, header[4]:header[4]:1].values)
   data.species3 = np.array(df.loc[:, header[5]:header[5]:1].values)
   data.flag3 = np.array(df.loc[:, header[6]:header[6]:1].values)
   data.species4 = np.array(df.loc[:, header[7]:header[7]:1].values)
   data.flag4 = np.array(df.loc[:, header[8]:header[8]:1].values)
   data.species5 = np.array(df.loc[:, header[9]:header[9]:1].values)
   data.flag5 = np.array(df.loc[:, header[10]:header[10]:1].values)
   data.species6 = np.array(df.loc[:, header[11]:header[11]:1].values)
   data.flag6 = np.array(df.loc[:, header[12]:header[12]:1].values)
   data.species7 = np.array(df.loc[:, header[13]:header[13]:1].values)
   data.flag7 = np.array(df.loc[:, header[14]:header[14]:1].values)
   data.species8 = np.array(df.loc[:, header[15]:header[15]:1].values)
   data.flag8 = np.array(df.loc[:, header[16]:header[16]:1].values)
   data.species9 = np.array(df.loc[:, header[17]:header[17]:1].values)
   data.flag9 = np.array(df.loc[:, header[18]:header[18]:1].values)
   data.species10 = np.array(df.loc[:, header[19]:header[19]:1].values)
   data.flag10 = np.array(df.loc[:, header[20]:header[20]:1].values)
   data.species11 = np.array(df.loc[:, header[21]:header[21]:1].values)
   data.flag11 = np.array(df.loc[:, header[22]:header[22]:1].values)
   
   if 'ppm' in header[1]:
      data.unit1 = '1e-6'
      data.practical_units1 = 'ppm'
   if 'ppb' in header[1]:
      data.unit1 = '1e-9'
      data.practical_units1 = 'ppb'
   if 'ppt' in header[1]:
      data.unit1 = '1e-12'
      data.practical_units1 = 'ppt'
   else:
      data.unit1 = '1e-12'
      data.practical_units1 = 'ppt'
   
   if 'ppm' in header[3]:
      data.unit2 = '1e-6'
      data.practical_units2 = 'ppm'
   if 'ppb' in header[3]:
      data.unit2 = '1e-9'
      data.practical_units2 = 'ppb'
   if 'ppt' in header[3]:
      data.unit2 = '1e-12'
      data.practical_units2 = 'ppt'
   else:
      data.unit2 = '1e-12'
      data.practical_units2 = 'ppt'
    
   if 'ppm' in header[5]:
      data.unit3 = '1e-6'
      data.practical_units3 = 'ppm'
   if 'ppb' in header[5]:
      data.unit3 = '1e-9'
      data.practical_units3 = 'ppb'
   if 'ppt' in header[5]:
      data.unit3 = '1e-12'
      data.practical_units3 = 'ppt'
   else:
      data.unit3 = '1e-12'
      data.practical_units3 = 'ppt'      
      
   if 'ppm' in header[7]:
      data.unit4 = '1e-6'
      data.practical_units4 = 'ppm'
   if 'ppb' in header[7]:
      data.unit4 = '1e-9'
      data.practical_units4 = 'ppb'
   if 'ppt' in header[7]:
      data.unit4 = '1e-12'
      data.practical_units4 = 'ppt'
   else:
      data.unit4 = '1e-12'
      data.practical_units4 = 'ppt'
      
   if 'ppm' in header[9]:
      data.unit5 = '1e-6'
      data.practical_units5 = 'ppm'
   if 'ppb' in header[9]:
      data.unit5 = '1e-9'
      data.practical_units5 = 'ppb'
   if 'ppt' in header[9]:
      data.unit5 = '1e-12'
      data.practical_units5 = 'ppt'
   else:
      data.unit5 = '1e-12'
      data.practical_units5 = 'ppt'
      
   if 'ppm' in header[11]:
      data.unit6 = '1e-6'
      data.practical_units6 = 'ppm'
   if 'ppb' in header[11]:
      data.unit6 = '1e-9'
      data.practical_units6 = 'ppb'
   if 'ppt' in header[11]:
      data.unit6 = '1e-12'
      data.practical_units6 = 'ppt'
   else:
      data.unit6 = '1e-12'
      data.practical_units6 = 'ppt'
      
   if 'ppm' in header[13]:
      data.unit7 = '1e-6'
      data.practical_units7 = 'ppm'
   if 'ppb' in header[13]:
      data.unit7 = '1e-9'
      data.practical_units7 = 'ppb'
   if 'ppt' in header[13]:
      data.unit7 = '1e-12'
      data.practical_units7 = 'ppt'
   else:
      data.unit7 = '1e-12'
      data.practical_units7 = 'ppt'
      
   if 'ppm' in header[15]:
      data.unit8 = '1e-6'
      data.practical_units8 = 'ppm'
   if 'ppb' in header[15]:
      data.unit8 = '1e-9'
      data.practical_units8 = 'ppb'
   if 'ppt' in header[15]:
      data.unit8 = '1e-12'
      data.practical_units8 = 'ppt'
   else:
      data.unit8 = '1e-12'
      data.practical_units8 = 'ppt'
      
   if 'ppm' in header[17]:
      data.unit9 = '1e-6'
      data.practical_units9 = 'ppm'
   if 'ppb' in header[17]:
      data.unit9 = '1e-9'
      data.practical_units9 = 'ppb'
   if 'ppt' in header[17]:
      data.unit9 = '1e-12'
      data.practical_units9 = 'ppt'
   else:
      data.unit9 = '1e-12'
      data.practical_units9 = 'ppt'
      
   if 'ppm' in header[19]:
      data.unit10 = '1e-6'
      data.practical_units10 = 'ppm'
   if 'ppb' in header[19]:
      data.unit10 = '1e-9'
      data.practical_units10 = 'ppb'
   if 'ppt' in header[19]:
      data.unit10 = '1e-12'
      data.practical_units10 = 'ppt'
   else:
      data.unit10 = '1e-12'
      data.practical_units10 = 'ppt'
      
   if 'ppm' in header[21]:
      data.unit11 = '1e-6'
      data.practical_units11 = 'ppm'
   if 'ppb' in header[21]:
      data.unit11 = '1e-9'
      data.practical_units11 = 'ppb'
   if 'ppt' in header[21]:
      data.unit11 = '1e-12'
      data.practical_units11 = 'ppt'
   else:
      data.unit11 = '1e-12'
      data.practical_units11 = 'ppt'
      
   data.ET = np.array(ET)
   data.DT = np.array(DT)
   data.DoY = np.array(DoY)
   
   return data    
   
def data_chunker(config, data, logfile):  
   import numpy as np

   st = []; ed = [] # holding array for start and stop points

   # all data
   if config[2] == 'all':
      # year long files
      if config[1] == 'year':
         st.append(0)
         for n in range (1, len(data.ET)):
            if data.DT[n, 0] != data.DT[n-1, 0]:
               st.append(n)
               ed.append(n)
         if len(st) != len(ed):
            ed.append(len(data.ET) - 1)   
      # month long files
      if config[1] == 'month':
         st.append(0)
         for n in range (1, len(data.ET)):
            if data.DT[n, 1] != data.DT[n-1, 1]:
               st.append(n)
               ed.append(n)
         if len(st) != len(ed):
            ed.append(len(data.ET) - 1)
      # day long files
      if config[1] == 'day':
         st.append(0)
         for n in range (1, len(data.ET)):
            if data.DT[n, 2] != data.DT[n-1, 2]:
               st.append(n)
               ed.append(n)
         if len(st) != len(ed):
            ed.append(len(data.ET) - 1)
      # convert to np array of integer and save to data tuple   
      ST = np.array(st)
      ED = np.array(ed)
      
      data.st = ST
      data.ed = ED
   else: # specific date
      xx = str(config[2]).strip("[]").strip("'")
      xx = xx.split(",")
      
      # specific year
      if config[1] == 'year':
         for n in range (len(data.ET)):
            if data.DT[n, 0] == np.int(xx[2]):
               st.append(n)               
      # specific month
      if config[1] == 'month':
         for n in range (len(data.ET)):
            if data.DT[n, 1] == np.int(xx[1]):
               st.append(n)  
      # specific day
      if config[1] == 'day':
         for n in range (len(data.ET)):
            if data.DT[n, 2] == np.int(xx[0]):
               st.append(n)
      # convert to np array of integer and save to data tuple          
      ST = np.array(st)  
      
      data.st = ST[0]
      data.ed = ST[-1] + 1
      
   # add an initalise a counter 
   data.counter = -1
   
   #add the file version number
   data.ver = config[0]
   
   return data
 