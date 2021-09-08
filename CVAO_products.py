def create_NC_file(config, start_date, opt, logfile):
   from netCDF4 import Dataset
   from datetime import datetime
   import os.path
 
   dout = 'Data' # out put directory
   
   f1 = config[3] # instrument name
   f2 = 'wao' # platform
   if config[1] == 'day':
     f3 = datetime.fromtimestamp(int(start_date)).strftime('%Y%m%d') # date
   if config[1] == 'month':
     f3 = datetime.fromtimestamp(int(start_date)).strftime('%Y%m') # date
   if config[1] == 'year':
     f3 = datetime.fromtimestamp(int(start_date)).strftime('%Y') # date
   f4 = config[4] # data product
   f5 = 'v' + config[0] # file version number
   f6 = '.nc'
   if len(opt) < 1:
      f7 = f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+f5+f6  
   else:         
      f7 = f1+chr(95)+f2+chr(95)+f3+chr(95)+f4+chr(95)+opt+chr(95)+f5+f6
      
   fn = os.path.join(dout, ' '.join(map(str, f7)))
   
   try:   
      nc = Dataset(fn, "w",  format = "NETCDF4_CLASSIC") 
   except:
      # exit if problem encountered
      print('Unable to create: ',fn,'. This program will terminate')
      g = open(logfile, 'a')
      g.write(datetime.utcnow().isoformat()+' Unable to create: '+fn+'. This program will terminate\n')
      g.close()
      exit()
      
      del Dataset, datetime

   return nc

# A# B# C# D# E# F# G# H# I# J# K# L# M# N# O# P# Q# R# S# T# U
# V
def voc_concentration(meta, data, nc):
   import CVAO_common as com
   import numpy as np
   
   # data, flag, time
   if data.counter == -1: #single day month or year
      ET =   data.ET[data.st:data.ed]
      DD1 =  data.species1[data.st:data.ed]
      FL1 =  data.flag1[data.st:data.ed]
      DD2 =  data.species2[data.st:data.ed]
      FL2 =  data.flag2[data.st:data.ed]
      DD3 =  data.species3[data.st:data.ed]
      FL3 =  data.flag3[data.st:data.ed]
      DD4 =  data.species4[data.st:data.ed]
      FL4 =  data.flag4[data.st:data.ed]
      DD5 =  data.species5[data.st:data.ed]
      FL5 =  data.flag5[data.st:data.ed]
      DD6 =  data.species6[data.st:data.ed]
      FL6 =  data.flag6[data.st:data.ed]
      DD7 =  data.species7[data.st:data.ed]
      FL7 =  data.flag7[data.st:data.ed]
      DD8 =  data.species8[data.st:data.ed]
      FL8 =  data.flag8[data.st:data.ed]
      DD9 =  data.species9[data.st:data.ed]
      FL9 =  data.flag9[data.st:data.ed]
      DD10 = data.species10[data.st:data.ed]
      FL10 = data.flag10[data.st:data.ed]
      DD11 = data.species11[data.st:data.ed]
      FL11 = data.flag11[data.st:data.ed]     
   else: # part of a multi file loop 
      ET =   data.ET[data.st[data.counter]:data.ed[data.counter]]
      DD1 =  data.species1[data.st[data.counter]:data.ed[data.counter]]
      FL1 =  data.flag1[data.st[data.counter]:data.ed[data.counter]]
      DD2 =  data.species2[data.st[data.counter]:data.ed[data.counter]]
      FL2 =  data.flag2[data.st[data.counter]:data.ed[data.counter]]
      DD3 =  data.species3[data.st[data.counter]:data.ed[data.counter]]
      FL3 =  data.flag3[data.st[data.counter]:data.ed[data.counter]]
      DD4 =  data.species4[data.st[data.counter]:data.ed[data.counter]]
      FL4 =  data.flag4[data.st[data.counter]:data.ed[data.counter]]
      DD5 =  data.species5[data.st[data.counter]:data.ed[data.counter]]
      FL5 =  data.flag5[data.st[data.counter]:data.ed[data.counter]]
      DD6 =  data.species6[data.st[data.counter]:data.ed[data.counter]]
      FL6 =  data.flag6[data.st[data.counter]:data.ed[data.counter]]
      DD7 =  data.species7[data.st[data.counter]:data.ed[data.counter]]
      FL7 =  data.flag7[data.st[data.counter]:data.ed[data.counter]]
      DD8 =  data.species8[data.st[data.counter]:data.ed[data.counter]]
      FL8 =  data.flag8[data.st[data.counter]:data.ed[data.counter]]
      DD9 =  data.species9[data.st[data.counter]:data.ed[data.counter]]
      FL9 =  data.flag9[data.st[data.counter]:data.ed[data.counter]]
      DD10 = data.species10[data.st[data.counter]:data.ed[data.counter]]
      FL10 = data.flag10[data.st[data.counter]:data.ed[data.counter]]
      DD11 = data.species11[data.st[data.counter]:data.ed[data.counter]]
      FL11 = data.flag11[data.st[data.counter]:data.ed[data.counter]]
      
   # valid max and min values
   XX1 = np.array(DD1)
   try:
      np.putmask(XX1, FL1 != 1, np.nan)
      min_dat1 = np.float32(np.nanmin(XX1))
      max_dat1 = np.float32(np.nanmax(XX1))    
   except:
      min_dat1 = np.float32(np.min(XX1))
      max_dat1 = np.float32(np.max(XX1)) 
   
   XX2 = np.array(DD2)
   try:
      np.putmask(XX2, FL2 != 1, np.nan)
      min_dat2 = np.float32(np.nanmin(XX2))
      max_dat2 = np.float32(np.nanmax(XX2))
   except:
      min_dat2 = np.float32(np.min(XX2))
      max_dat2 = np.float32(np.max(XX2))
      
   XX3 = np.array(DD3)
   try:
      np.putmask(XX3, FL3 != 1, np.nan)
      min_dat3 = np.float32(np.nanmin(XX3))
      max_dat3 = np.float32(np.nanmax(XX3))
   except:
      min_dat3 = np.float32(np.min(XX3))
      max_dat3 = np.float32(np.max(XX3))
   
   XX4 = np.array(DD4)
   try:
      np.putmask(XX4, FL4 != 1, np.nan)
      min_dat4 = np.float32(np.nanmin(XX4))
      max_dat4 = np.float32(np.nanmax(XX4))
   except:
      min_dat4 = np.float32(np.min(XX4))
      max_dat4 = np.float32(np.max(XX4))
      
   XX5 = np.array(DD5)
   try:
      np.putmask(XX5, FL5 != 1, np.nan)
      min_dat5 = np.float32(np.nanmin(XX5))
      max_dat5 = np.float32(np.nanmax(XX5))
   except:
      min_dat5 = np.float32(np.min(XX5))
      max_dat5 = np.float32(np.max(XX5))
   
   XX6 = np.array(DD6)
   try:
      np.putmask(XX6, FL6 != 1, np.nan)
      min_dat6 = np.float32(np.nanmin(XX6))
      max_dat6 = np.float32(np.nanmax(XX6))
   except:
      min_dat6 = np.float32(np.min(XX6))
      max_dat6 = np.float32(np.max(XX6))
   
   XX7 = np.array(DD7)
   try:
      np.putmask(XX7, FL7 != 1, np.nan)   
      min_dat7 = np.float32(np.nanmin(XX7))
      max_dat7 = np.float32(np.nanmax(XX7))
   except:
      min_dat7 = np.float32(np.min(XX7))
      max_dat7 = np.float32(np.max(XX7))
   
   XX8 = np.array(DD8)
   try:
      np.putmask(XX8, FL8 != 1, np.nan)
      min_dat8 = np.float32(np.nanmin(XX8))
      max_dat8 = np.float32(np.nanmax(XX8))
   except:
      min_dat8 = np.float32(np.min(XX8))
      max_dat8 = np.float32(np.max(XX8))
   
   XX9 = np.array(DD9)
   try:
      np.putmask(XX9, FL9 != 1, np.nan)
      min_dat9 = np.float32(np.nanmin(XX9))
      max_dat9 = np.float32(np.nanmax(XX9))
   except:
      min_dat9 = np.float32(np.min(XX9))
      max_dat9 = np.float32(np.max(XX9))
      
   XX10 = np.array(DD10)
   try:
      np.putmask(XX10, FL10 != 1, np.nan)
      min_dat10 = np.float32(np.nanmin(XX10))
      max_dat10 = np.float32(np.nanmax(XX10))
   except:
      min_dat10 = np.float32(np.min(XX10))
      max_dat10 = np.float32(np.max(XX10))
   
   XX11 = np.array(DD11)
   try:
      np.putmask(XX11, FL11 != 1, np.nan)
      min_dat11 = np.float32(np.nanmin(XX11))
      max_dat11 = np.float32(np.nanmax(XX11))
   except:
      min_dat11 = np.float32(np.min(XX11))
      max_dat11 = np.float32(np.max(XX11))
   # write common global attrib 
   com.global_attributes(nc, meta, ET)
 
   # write specific global attrib
   nc.product_version = ' '.join(map(str, data.ver))
      
   # write common dimensions
   com.dimensions(nc, ET)
   
   # write common variables
   com.variables(nc, data)
   
   # write specific variables
   v = nc.createVariable('mole_fraction_of_ethane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit1
   v.practical_units = data.practical_units1
   v.standard_name = 'mole_fraction_of_ethane_in_air'
   v.long_name = 'Mole Fraction of Ethane in air'
   v.valid_min = np.float32(min_dat1)
   v.valid_max = np.float32(max_dat1)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C2H6'
   # write data
   v[:] = np.float32(DD1)
   
   v = nc.createVariable('mole_fraction_of_ethene_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit2
   v.practical_units = data.practical_units2
   v.standard_name = 'mole_fraction_of_ethene_in_air'
   v.long_name = 'Mole Fraction of Ethene in air'
   v.valid_min = np.float32(min_dat2)
   v.valid_max = np.float32(max_dat2)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C2H4'
   # write data
   v[:] = np.float32(DD2)
   
   v = nc.createVariable('mole_fraction_of_propane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit3
   v.practical_units = data.practical_units3
   v.standard_name = 'mole_fraction_of_propane_in_air'
   v.long_name = 'Mole Fraction of Propane in air'
   v.valid_min = np.float32(min_dat3)
   v.valid_max = np.float32(max_dat3)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C3H8'
   # write data
   v[:] = np.float32(DD3)
   
   v = nc.createVariable('mole_fraction_of_propene_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit4
   v.practical_units = data.practical_units4
   v.standard_name = 'mole_fraction_of_propene_in_air'
   v.long_name = 'Mole Fraction of Propene in air'
   v.valid_min = np.float32(min_dat4)
   v.valid_max = np.float32(max_dat4)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C3H6'
   # write data
   v[:] = np.float32(DD4)
   
   v = nc.createVariable('mole_fraction_of_iso_butane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit5
   v.practical_units = data.practical_units5
   v.long_name = 'Mole Fraction of iso-Butane in air'
   v.valid_min = np.float32(min_dat5)
   v.valid_max = np.float32(max_dat5)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C4H10'
   # write data
   v[:] = np.float32(DD5)
   
   v = nc.createVariable('mole_fraction_of_n_butane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit6
   v.practical_units = data.practical_units6
   v.long_name = 'Mole Fraction of n-Butane in air'
   v.valid_min = np.float32(min_dat6)
   v.valid_max = np.float32(max_dat6)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C4H10'
   # write data
   v[:] = np.float32(DD6)
   
   v = nc.createVariable('mole_fraction_of_acetylene_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit7
   v.practical_units = data.practical_units7
   v.long_name = 'Mole Fraction of Acetylene in air'
   v.valid_min = np.float32(min_dat7)
   v.valid_max = np.float32(max_dat7)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C2H2'
   # write data
   v[:] = np.float32(DD7)
   
   v = nc.createVariable('mole_fraction_of_iso_pentane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit8
   v.practical_units = data.practical_units8
   v.long_name = 'Mole Fraction of iso-Pentane in air'
   v.valid_min = np.float32(min_dat8)
   v.valid_max = np.float32(max_dat8)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C5H12'
   # write data
   v[:] = np.float32(DD8)
   
   v = nc.createVariable('mole_fraction_of_n_pentane_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit9
   v.practical_units = data.practical_units9
   v.long_name = 'Mole Fraction of n-Pentane in air'
   v.valid_min = np.float32(min_dat9)
   v.valid_max = np.float32(max_dat9)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C5H12'
   # write data
   v[:] = np.float32(DD9)
   
   v = nc.createVariable('mole_fraction_of_benzene_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit10
   v.practical_units = data.practical_units10
   v.standard_name = 'mole_fraction_of_benzene_in_air'
   v.long_name = 'Mole Fraction of Benzene in air'
   v.valid_min = np.float32(min_dat10)
   v.valid_max = np.float32(max_dat10)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C6H6'
   # write data
   v[:] = np.float32(DD10)
   
   v = nc.createVariable('mole_fraction_of_toluene_in_air', np.float32, ('time',), fill_value=-1.00e+20)
   # variable attributes
   v.units = data.unit11
   v.practical_units = data.practical_units11
   v.standard_name = 'mole_fraction_of_toluene_in_air'
   v.long_name = 'Mole Fraction of Toluene in air'
   v.valid_min = np.float32(min_dat11)
   v.valid_max = np.float32(max_dat11)
   v.cell_methods = 'time: point'
   v.coordinates = 'latitude longitude'
   v.chemical_species = 'C7H8'
   # write data
   v[:] = np.float32(DD11)
   
   v = nc.createVariable('qc_flag_c2h6', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: C2H6'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL1)
   
   v = nc.createVariable('qc_flag_c2h4', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: C2H4'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL2)
   
   v = nc.createVariable('qc_flag_c3h8', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: C2H6'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL3)
   
   v = nc.createVariable('qc_flag_c3h6', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: C3H6'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL4)
   
   v = nc.createVariable('qc_flag_iso_c4h10', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: iso-C4H10'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL5)
   
   v = nc.createVariable('qc_flag_n_c4h10', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: n-C4H10'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL6)
   
   v = nc.createVariable('qc_flag_c2h2', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: C2H2'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL7)
   
   v = nc.createVariable('qc_flag_iso_c5h12', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: iso-C5H12'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL8)
   
   v = nc.createVariable('qc_flag_n_c5h12', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: n-C5H12'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL9)
   
   v = nc.createVariable('qc_flag_c6h6', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: C6H6'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason'  
   # write data
   v[:] = np.int8(FL10)
   
   v = nc.createVariable('qc_flag_c7h8', np.int8, ('time',))
   # variable attribute
   v.units = '1'
   v.long_name = 'Data Quality Flag: C7H8'
   v.flag_values = '0b,1b,2b,3b,4b'
   v.flag_meanings = '0:not_used' + '\n'
   v.flag_meanings = v.flag_meanings + '1:good_data' + '\n'
   v.flag_meanings = v.flag_meanings + '2:suspect_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '3:bad_data_give_the_reason' + '\n'
   v.flag_meanings = v.flag_meanings + '4:suspect_data_give_the_reason' 
   # write data
   v[:] = np.int8(FL11)

# W# X# Y# Z
