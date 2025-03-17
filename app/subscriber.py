import redis
import threading

# Connect to Redis server
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# # Subscribe to a channel
# pubsub = r.pubsub()
# pubsub.subscribe('my_channel')

# # Function to handle messages received from Redis Pub/Sub
# def handle_message(message):
#     print(f"Received message: {message['data']}")

# # Start a separate thread to listen for messages
# def listen_for_messages():
#     for message in pubsub.listen():
#         if message['type'] == 'message':
#             handle_message(message)

# thread = threading.Thread(target=listen_for_messages)
# thread.start()


# Subscribe to multiple channels
# Define a pattern to subscribe to
pattern = 'my_*'

# Subscribe to channels matching the pattern
pubsub = r.pubsub()
pubsub.psubscribe(pattern)

# Start a separate thread to listen for messages
def listen_for_pmessages():
    for message in pubsub.listen():
        if message['type'] == 'pmessage':
            print(f"Pattern: {message['pattern']}, Channel: {message['channel']}, Message: {message['data']}")

thread = threading.Thread(target=listen_for_pmessages)
thread.start()
