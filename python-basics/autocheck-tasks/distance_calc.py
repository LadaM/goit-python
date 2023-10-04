import math

RADIUS = 6371.01

lat1 = 50.45
lon1 = 30.523

lat2 = 51.5072
lon2 = -0.1275

rad_lat1 = math.radians(lat1)
rad_lat2 = math.radians(lat2)
rad_lon1 = math.radians(lon1)
rad_lon2 = math.radians(lon2)

distance = RADIUS * math.acos(
    math.sin(rad_lat1) * math.sin(rad_lat2) + 
    math.cos(rad_lat1) * math.cos(rad_lat2) * math.cos(rad_lon1 - rad_lon2))