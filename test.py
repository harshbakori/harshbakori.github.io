from sgp4.api import Satrec
from sgp4.api import jday
import navpy
import numpy as np

#ISS

s = '1 25544U 98067A   21336.70775771  .00004247  00000-0  85987-4 0  9994'
t = '2 25544  51.6437 229.4568 0004362 271.6918 182.8759 15.48732282314711'
satellite = Satrec.twoline2rv(s, t)

jd, fr = jday(2021, 12, 8, 9, 4, 0)
e, r, v = satellite.sgp4(jd, fr) # e = error, r = position vector, v = speed vector

print("e = ",e)
print("r = ",r)
print("v = ",v)


lat, lon, alt = 48.1, 16.3, 250 
r0 = navpy.lla2ecef(lat, lon, alt, latlon_unit='deg', alt_unit='m', model='wgs84')

x, y, z = r - r0
az = np.arctan2(x,y)
el = np.arctan2(z,y)
az_deg = 180*az/np.pi
el_deg = 180*el/np.pi

print("r-r0",r-r0)
print("az",az)
print("el",el)
print("az_deg",az_deg)
print("el_deg",el_deg)
