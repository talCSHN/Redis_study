import redis

# Establish connection to Redis
r = redis.Redis(host='redis-stack', port=6379, db=0, decode_responses=True)

# bloom filter
bf = r.bf()

# Create a Bloom filter named 'bloom' with a desired error rate of 0.01 and an initial capacity of 100 items
bf.create("bloom", 0.01, 100)

# Add elements to the Bloom filter
bf.add("bloom", "apple")
bf.add("bloom", "banana")
bf.add("bloom", "cherry")

# Test for element membership
print("apple exists:", bf.exists('bloom', 'apple'))  # Should return: True
print("banana exists:", bf.exists('bloom', 'banana'))  # Should return: True
print("cherry exists:", bf.exists('bloom', 'cherry'))  # Should return: True
print("lemon exists:", bf.exists('bloom', 'lemon'))  # Should return: False

# cuckoo filter
cf = r.cf()
cf.add("bikes:models", "Smoky Mountain Striker")
print("Smoky Mountain Striker exists:", cf.exists("bikes:models", "Smoky Mountain Striker"))
print("Terrible Bike Name exists:", cf.exists("bikes:models", "Terrible Bike Name"))
cf.delete("bikes:models", "Smoky Mountain Striker")
print("Smoky Mountain Striker exists:", cf.exists("bikes:models", "Smoky Mountain Striker"))
