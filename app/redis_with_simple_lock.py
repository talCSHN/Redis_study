import redis
import time

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

def acquire_lock(lock_name, acquire_timeout=10):
    """Attempt to acquire a lock with the given name."""
    lock_key = f"lock:{lock_name}"
    while True:
        # Attempt to acquire the lock
        if r.set(lock_key, "locked", ex=acquire_timeout, nx=True):
            return True
        # Sleep for a short interval before retrying
        time.sleep(0.1)

def release_lock(lock_name):
    """Release the lock with the given name."""
    lock_key = f"lock:{lock_name}"
    # Delete the lock key
    r.delete(lock_key)

# Example usage:
if acquire_lock("my_lock"):
    try:
        # Critical section - do some work here
        print("Lock acquired, performing critical section...")
        time.sleep(5)  # Simulate some work
    finally:
        print("Lock is released...")
        release_lock("my_lock")
else:
    print("Failed to acquire lock, another process is holding the lock.")
