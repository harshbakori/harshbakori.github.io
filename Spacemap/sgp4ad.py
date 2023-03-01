from sgp4.api import Satrec
from sgp4.api import jday


# ISS (ZARYA)             

s = '1 25544U 98067A   23055.36715531  .00017001  00000+0  31285-3 0  9996'
t = '2 25544  51.6387 167.3561 0005418  22.9195  99.0673 15.49284681384295'
satellite = Satrec.twoline2rv(s, t)



# jd, fr = jday(2019, 12, 9, 12, 0, 0)

# jd, fr = 2458827, 0.362605
# e, r, v = satellite.sgp4(jd, fr)
# print(e)
# print(r)  # True Equator Mean Equinox position (km)
# print(v)  # True Equator Mean Equinox velocity (km/s)
# print("satellite = ",satellite)
print("satellite.epochyr = ",satellite.epochyr)
print("satellite.epochdays = ", satellite.epochdays)

# ===============================================================================
from sgp4.conveniences import sat_epoch_datetime
print(sat_epoch_datetime(satellite))

# u = '1 20580U 90037B   19342.88042116  .00000361  00000-0  11007-4 0  9996'
# w = '2 20580  28.4682 146.6676 0002639 185.9222 322.7238 15.09309432427086'
# satellite2 = Satrec.twoline2rv(u, w)

# from sgp4.api import SatrecArray
# a = SatrecArray([satellite, satellite2])
# # e, r, v = a.sgp4(jd, fr)

# import numpy as np
# np.set_printoptions(precision=2)
# jd = np.array((2458826, 2458826, 2458826, 2458826))
# fr = np.array((0.0001, 0.0002, 0.0003, 0.0004))
# # e, r, v = satellite.sgp4_array(jd, fr)
# e, r, v = a.sgp4(jd, fr)

# np.set_printoptions(precision=3)
# # print(e,r,v)

# from sgp4 import exporter
# line1, line2 = exporter.export_tle(satellite)
# print(line1, line2)

# from pprint import pprint
# fields = exporter.export_omm(satellite, 'ISS (ZARYA)')
# pprint(fields)





from sys import stdout
from sgp4.conveniences import dump_satrec

stdout.writelines(dump_satrec(satellite))

{
    "position":"",  #in relevance of the center obj
    "motion":"",  #in relevance of the center obj
    "name":"",
    "id":"",
}