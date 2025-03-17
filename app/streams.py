import redis
import time

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

stream_key = 'mystream'
r.delete(stream_key)

# Add messages to a stream
messages = [
    {'field1': 'value1', 'field2': 'value2'},
    {'field1': 'value3', 'field2': 'value4'},
    {'field1': 'value5', 'field2': 'value6'}
]
for message in messages:
    r.xadd(stream_key, message) # type: ignore

# Read messages from the stream
# Start reading from the beginning
stream_range = r.xrange(stream_key, min='-', max='+') # type: ignore
for message_id, fields in stream_range: # type: ignore
    print(f"Message ID: {message_id}, Fields: {fields}")

