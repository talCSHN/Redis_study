import time
from redlock import Redlock

class RedlockHelper(object):
    def __init__(self):
        # Create a RedLock instance with connection details to your Redis servers
        # You can specify multiple Redis servers for fault tolerance
        servers = [
            {"host": "redis", "port": 6379, "db": 0}
        ]
        self.dlm = Redlock(servers)
        self.my_lock = None

    def acquire_lock(self, lock_name, ttl=5000):
        """Attempt to acquire a lock with the given name."""
        lock_key = f"lock:{lock_name}"
        while True:
            self.my_lock = self.dlm.lock(lock_key, ttl)
            if self.my_lock:
                return True
            # Sleep for a short interval before retrying
            time.sleep(0.1)

    def release_lock(self):
        """Release the lock with the given name."""
        # Delete the lock key
        self.dlm.unlock(self.my_lock)

if __name__ == "__main__":
    redlockHelper = RedlockHelper()
    if redlockHelper.acquire_lock("my_lock"):
        try:
            # Critical section - do some work here
            print("Lock acquired, performing critical section...")
            time.sleep(5)  # Simulate some work
        finally:
            print("Lock is released...")
            redlockHelper.release_lock()
    else:
        print("Failed to acquire lock, another process is holding the lock.")
