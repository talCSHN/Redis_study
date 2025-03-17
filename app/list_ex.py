import redis

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

r.delete('mylist')

# Add elements to the list
r.lpush('mylist', 'element1')
r.rpush('mylist', 'element2')
"""
element1 <-> element2
"""

# Retrieve elements from the list
element_at_index_0 = r.lindex('mylist', 0)
print("Element at index 0:", element_at_index_0)

# Get the length of the list
list_length = r.llen('mylist')
print("Length of the list:", list_length)

# Pop elements from the list
popped_element_left = r.lpop('mylist')
popped_element_right = r.rpop('mylist')
print("Popped element from left:", popped_element_left)
"""
element2
"""
print("Popped element from right:", popped_element_right)
"""
empty
"""

# Add multiple elements to the list
r.lpush('mylist', 'element3', 'element4', 'element5', 'element4')
"""
element4 <-> element5 <-> element4 <-> element3
"""
# Retrieve a range of elements from the list
elements_range = r.lrange('mylist', 0, -1)
print("Elements in the list:", [element for element in elements_range])

r.delete('fruits')

# Add some elements to the list
r.rpush('fruits', 'apple', 'banana', 'apple', 'apple', 'banana', 'orange', 'apple')
"""
apple <-> banana <-> apple <-> apple <-> banana <-> orange <-> apple
"""

# Find the 2-based position of 'apple' in the list
position_rank_2 = r.lpos('fruits', 'apple', rank=2)
print("2-based position of 'apple' in the list:", position_rank_2)

# Find the position of 'banana' in the list with MAXLEN=4
position_maxlen = r.lpos('fruits', 'banana', maxlen=4)
print("Position of 'banana' in the list (MAXLEN=4):", position_maxlen)

# Find the position of the second occurrence of 'apple' in the list
position_count = r.lpos('fruits', 'apple', count=2)
print("Position of the second occurrence of 'apple' in the list:", position_count)

# Set the value of the element at index 2 to "pineapple"
r.lset('fruits', 2, 'pineapple')
print("New value in index 2:", r.lindex('fruits', 2))
"""
apple <-> banana <-> pineapple <-> apple <-> banana <-> orange <-> apple
"""

# Trim the list to contain only elements from index 1 to 2
r.ltrim('fruits', 1, 2)
print("After trimming: ", r.lrange('fruits', 0, -1))
"""
banana <-> pineapple
"""

# Insert "dragonfruit" before "pineapple"
result_before = r.linsert('fruits', 'BEFORE', 'pineapple', 'dragonfruit')
print("Result of insertion", r.lrange('fruits', 0, -1))
"""
banana <-> dragonfruit <-> pineapple
"""

# Insert "watermelon" after "pineapple"
result_after = r.linsert('fruits', 'AFTER', 'pineapple', 'watermelon')
print("Result of insertion", r.lrange('fruits', 0, -1))
"""
banana <-> dragonfruit <-> pineapple <-> watermelon
"""

# Remove all occurrences of "watermelon" from the list
removed_count = r.lrem('fruits', 0, 'watermelon')
print("Number of elements removed:", removed_count)
print("Result of deletion", r.lrange('fruits', 0, -1))
"""
banana <-> dragonfruit <-> pineapple
"""