from skyfield.api import load, wgs84

stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
# satellites = load.tle_file(stations_url,reload=True)
satellites = load.tle_file(stations_url)



print('Loaded', len(satellites), 'satellites')

by_name = {sat.name: sat for sat in satellites}
satellite = by_name['ISS (ZARYA)']
print(satellite)

from sgp4.api import Satrec
# s = '1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991'
# t = '2 25544  51.6439 211.2001 0007417  17.6667  85.6398 15.50103472202482'
# satellite = Satrec.twoline2rv(s, t)
# jd, fr = 2458827, 0.362605
# e, r, v = satellite.sgp4(jd, fr)
# e
# print(r)  # True Equator Mean Equinox position (km)
# print(v)  # True Equator Mean Equinox velocity (km/s)


# by_number = {sat.model.satnum: sat for sat in satellites}
# satellite = by_number[25544]
# print(satellite)


# # =====================================================================================================
# from skyfield.api import EarthSatellite

ts = load.timescale()
# line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
# line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
# satellite = EarthSatellite(line1, line2, 'ISS (ZARYA)', ts)
# print(satellite)
# print(satellite.epoch.utc_jpl())
# # print(ts.now() - satellite.epoch)

# # # ====================================================================================================
# geocentric = satellite.at(ts.now())
# print(geocentric.position.km)


from pprint import pprint

geocentric = satellite.at(ts.utc(2013, 11, [9, 10, 11, 12, 13]))
pprint(geocentric.message)


# lat, lon = wgs84.latlon_of(geocentric)
# print('Latitude:', lat)
# print('Longitude:', lon)
# # print('eslevation:', elv)
# gioposition = wgs84.geographic_position_of(geocentric)

# wgs84.g

# print('gioposition',gioposition)