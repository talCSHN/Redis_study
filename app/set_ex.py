import redis

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# Add elements to a set
r.sadd('myset', 1, 2, 3, 4, 5)

# Check if an element exists in the set
print(r.sismember('myset', 3))  # 1

# Remove elements from a set
r.srem('myset', 2, 4)

# Get all members of a set
print(r.smembers('myset'))  # {'1', '3', '5'}

# Get the number of elements in a set
print(r.scard('myset'))  # 3

# Create two sets
r.sadd('set1', 1, 2, 3, 4)
r.sadd('set2', 3, 4, 5, 6)

# Set intersection
intersection = r.sinter('set1', 'set2')
print("Intersection:", intersection)  # Intersection: {'3', '4'}

# Set union
union = r.sunion('set1', 'set2')
print("Union:", union)  # Union: {'1', '5', '6', '2', '3', '4'}

# Set difference
diff = r.sdiff('set1', 'set2')
print("Difference:", diff)  # Difference: {'1', '2'}

# Compute the union of set1 and set2 and store the result in a new set named union_result
r.sunionstore('union_result', 'set1', 'set2')
print("Union Result:", r.smembers('union_result'))  # Union Result: {'5', '6', '1', '4', '2', '3'}

# Compute the difference between set1 and set2 and store the result in a new set named diff_result
r.sdiffstore('diff_result', 'set1', 'set2')
print("Difference Result:", r.smembers('diff_result'))  # Difference Result: {'2', '1'}

# Compute the intersection of set1 and set2 and store the result in a new set named inter_result
r.sinterstore('inter_result', 'set1', 'set2')
print("Intersection Result:", r.smembers('inter_result'))  # Intersection Result: {'3', '4'}
