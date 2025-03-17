import redis

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# Your Lua script
lua_script = """
local key1 = KEYS[1]
local key2 = KEYS[2]
local increment = ARGV[1]
redis.call('DEL', key1)
redis.call('DEL', key2)
redis.call('INCRBY', key1, increment)
redis.call('INCRBY', key2, increment)

return redis.call('MGET', key1, key2)
"""
# The keys and arguments for the script
keys = ['key1', 'key2']
args = [5]

# Execute the script
result = r.eval(lua_script, len(keys), *keys, *args)

# Print the result
print(result)
