import redis

# Establish connection to Redis
r = redis.Redis(host='redis-stack', port=6379, db=0, decode_responses=True)

ts = r.ts()

# Create a timeseries
ts.create("ts_key")

# Add samples to the timeseries
ts.add("ts_key", 1657265437756, 1)
ts.add("ts_key", "1657265437757", 2)
ts.add("ts_key", "*", 3)

# Get the last sample
print(ts.get("ts_key"))

# # Get samples between two timestamps
# print(ts.range("ts_key", "-", "+"))
# print(ts.range("ts_key", 1657265437756, 1657265437757))

# # Delete samples between two timestamps
# print("Before deletion: ", ts.range("ts_key", "-", "+"))
# ts.delete("ts_key", 1657265437756, 1657265437757)
# print("After deletion:  ", ts.range("ts_key", "-", "+"))

# # Multiple timeseries with labels
# ts.create("ts_key1")
# ts.create("ts_key2", labels={"label1": 1, "label2": 2}) # type: ignore

# # Add samples to multiple timeseries
# ts.madd([("ts_key1", "*", 1), ("ts_key2", "*", 2)])

# # Add samples with labels (optional)
# ts.add("ts_key2", "*", 2,  labels={"label1": 1, "label2": 2}) # type: ignore
# ts.add("ts_key2", "*", 2,  labels={"label1": 3, "label2": 4}) # type: ignore

# # Get the last sample matching specific label
# print(ts.mget(["label1=1"], with_labels=True))

# # Retention period
# retention_time = 500
# # ts.create("ts_key_ret", retention_msecs=retention_time)

# import time
# # this will be deleted in 500 milliseconds
# ts.add("ts_key_ret", "*", 1, retention_msecs=retention_time)
# print("Base timeseries: ", ts.range("ts_key_ret", "-", "+"))
# # sleeping for 1000 milliseconds (1 second)
# time.sleep(1)
# print("Timeseries after 1000 milliseconds: ", ts.range("ts_key_ret", "-", "+"))

# # The two lists are the same, this is because the oldest values are deleted when a new sample is added.
# ts.add("ts_key_ret", "*", 10)
# ts.add("ts_key_ret", "*", 20)
# print("Old one is deleted: ", ts.range("ts_key_ret", "-", "+", aggregation_type='avg', bucket_size_msec=1000))

