import redis

# Connect to Redis server
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# Subscribe to a channel
pubsub = r.pubsub()

# Publish messages to the channel
while True:
    message = input("Enter message to publish (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    r.publish('my_channel', message)

pubsub.close()
