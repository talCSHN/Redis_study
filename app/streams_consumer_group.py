import redis
import time

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# Stream key and group name
stream_key = 'mystream'
group_name = 'mygroup'

# Add the first message with the custom message ID
first_message = {'field1': 'value1', 'field2': 'value2'}
r.xadd(stream_key, first_message) # type: ignore

# Get information about consumer groups associated with the stream
consumer_groups_info = r.execute_command('XINFO', 'GROUPS', stream_key)

# Check if the specified consumer group exists
group_exists = any(group[1] == group_name for group in consumer_groups_info)
if group_exists:
    print(f"Consumer group '{group_name}' exists.")
else:
    print(f"Consumer group '{group_name}' does not exist.")
    # Create a new consumer group
    created = r.xgroup_create(stream_key, group_name, id='0', mkstream=True)
    print(f"Consumer group '{group_name}' created: {created}")

# Add the first message with the custom message ID
first_message = {'field1': 'value1', 'field2': 'value2'}
r.xadd(stream_key, first_message) # type: ignore

consumer_name = 'consumer1'

# Read messages from the stream within the consumer group
stream_entries = r.xreadgroup(group_name, consumer_name, {stream_key: '>'}, count=10)
for stream, messages in stream_entries: # type: ignore
    print(f"Stream: {stream}")
    for message_id, fields in messages:
        print(f"Message ID: {message_id}, Fields: {fields}")
        acknowledged = r.xack(stream_key, group_name, message_id)
        print(f"Message '{message_id}' acknowledged: {acknowledged}")

first_message = {'field1': 'value1', 'field2': 'value2'}
r.xadd(stream_key, first_message) # type: ignore

# Read messages from the stream within the consumer group
stream_entries = r.xreadgroup(group_name, consumer_name, {stream_key: '>'}, count=10)
for stream, messages in stream_entries: # type: ignore
    print(f"=> After Acked Stream: {stream}")
    for message_id, fields in messages:
        print(f"Message ID: {message_id}, Fields: {fields}")


r.xgroup_destroy(stream_key, group_name)
r.delete(stream_key)
