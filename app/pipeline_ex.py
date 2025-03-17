import redis

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# Using pipelines for multiple operations
pipe = r.pipeline()

# Queue commands in the pipeline
pipe.set('name', 'Alice')
pipe.set('age', 30)
pipe.set('country', 'USA')
pipe.mset({'state': 'california', 'city': 'san francisco'})
pipe.mget(['state'])

# Execute the pipeline and fetch results
print(pipe.execute())
"""
[True, True, True, True, ['california']]
"""

# Get values using pipeline
values = r.mget('name', 'age', 'country', 'city')

# Print values
print("Name:", values[0])
print("Age:", values[1])
print("Country:", values[2])
print("City:", values[3])