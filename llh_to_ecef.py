# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Converts LLH vector components to ECEF
# Parameters:
# lat_deg 
# lon_deg 
# hae_km
#
# Output:
#  Prints the r_x_km, r_y_km, and r_z_km
#
# Written by Nicola Demarinis
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# "constants"
R_E_KM = 6378.1363
E_E    = 0.081819221456

# helper functions

## calculated denominator
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
lat_deg = float('nan') # ECEF x-component in km
lon_deg = float('nan') # ECEF y-component in km
hae_km = float('nan') # ECEF z-component in km

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
   'Usage: '\
   'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
  )
  exit()

# write script below this line
lat_rad = lat_deg*math.pi/180
lon_rad = lon_deg*math.pi/180

c_E = R_E_KM/calc_denom(E_E,lat_rad)
s_E = (R_E_KM*(1-E_E**2))/calc_denom(E_E,lat_rad)

r_x_km = (c_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (c_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (s_E+hae_km)*math.sin(lat_rad)

#r_km = math.sqrt(r_x_km**2 + r_y_km**2 + r_z_km**2)

# print latitude (deg), longitude (deg), and HAE (km)
print(r_x_km)
print(r_y_km)
print(r_z_km)
