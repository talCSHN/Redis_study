import redis

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

res1 = r.geoadd("bikes:rentable", [-122.27652, 37.805186, "station:1"])
# print(res1)  # >>> 1

res2 = r.geoadd("bikes:rentable", [-122.2674626, 37.8062344, "station:2"])
# print(res2)  # >>> 1

res3 = r.geoadd("bikes:rentable", [-122.2469854, 37.8104049, "station:3"])
# print(res3)  # >>> 1


res4 = r.geosearch(
    "bikes:rentable",
    longitude=-122.27652,
    latitude=37.805186,
    radius=5,
    unit="km",
)
print("Geo search: ", res4)  # >>> ['station:1', 'station:2', 'station:3']

# Geospatial key for storing locations
geo_key = 'cities'

# Add geospatial data (longitude, latitude, and name)
r.geoadd(geo_key, [13.361389, 38.115556, 'Palermo'])
r.geoadd(geo_key, [15.087269, 37.502669, 'Catania'])

# Perform a radius query: find locations within 100 km of a point (15 longitude, 37 latitude)
nearby_cities = r.georadius(geo_key, 15, 37, 100, unit='km', sort='ASC')
print('Cities within 100 km:', nearby_cities)

# Calculate the distance between two points
distance = r.geodist(geo_key, 'Palermo', 'Catania', unit='km')
print('Distance between Palermo and Catania:', distance, 'km')

# Fetch the geospatial position (latitude and longitude) of a member
palermo_pos = r.geopos(geo_key, 'Palermo')
catania_pos = r.geopos(geo_key, 'Catania')
print('Position of Palermo:', palermo_pos)
print('Position of Catania:', catania_pos)

# Perform a radius query by member: find locations within 200 km of 'Catania'
nearby_cities_by_member = r.georadiusbymember(geo_key, 'Catania', 200, unit='km')
print('Cities within 50 km of Catania:', nearby_cities_by_member)
