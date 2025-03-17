import redis

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

r.delete('unique_visitors')
# Add elements to the HyperLogLog
# return 1 if it is new, 0 otherwise
print(r.pfadd('unique_visitors', 'visitor1', 'visitor2', 'visitor3', 'visitor1'))

# Count the approximate number of unique visitors
approx_unique_visitors = r.pfcount('unique_visitors')
print("Approximate unique visitors:", approx_unique_visitors)

# Add more elements to the HyperLogLog
r.pfadd('unique_visitors', 'visitor4', 'visitor5')

# Count the updated approximate number of unique visitors
approx_unique_visitors = r.pfcount('unique_visitors')
print("Updated approximate unique visitors:", approx_unique_visitors)

# Create and add elements to HyperLogLog 1
r.pfadd('hll1', 'a', 'b', 'c', 'd', 'e')

# Create and add elements to HyperLogLog 2
r.pfadd('hll2', 'c', 'd', 'e', 'f', 'g')

# Union operation
r.pfmerge('hll_union', 'hll1', 'hll2')

# Count the approximate number of unique elements in the union
approx_union_count = r.pfcount('hll_union')
print("Approximate count of unique elements in the union:", approx_union_count)
