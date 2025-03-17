import redis

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# Set a key-value pair
r.set('name', 'Alice')

# Get the value of a key
name = r.get('name')
print("Name:", name)

# Increment the value of the key 'counter' by a specified amount
r.incrby('counter1', 5)
r.incrby('counter1', 5)
counter1 = r.get('counter1')
print("Counter1:", counter1)

r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})

print(r.hgetall('user-session:123'))

