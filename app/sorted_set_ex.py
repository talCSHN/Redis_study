import redis

# Establish connection to Redis
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

# cleanup the sorted set named 'leaderboard'
r.delete('leaderboard')

# Add a memeber to the sorted set
r.zadd('leaderboard', {'Alice': 100, 'Bob': 200, 'Carol': 150, 'Tom': 300})


# Remove a member from the sorted set
r.zrem('leaderboard', 'Carol')


# Retrieve the score of a member
alice_score = r.zscore('leaderboard', 'Alice')
print("Alice's score:", alice_score)
# Alice's score: 100.0


# Get the number of members in the sorted set
leaderboard_size = r.zcard('leaderboard')
print("Number of members in the leaderboard:", leaderboard_size)
# Number of members in the leaderboard: 3


# Count the number of members with scores between 120 and 200
members_in_range_count = r.zcount('leaderboard', 120, 200)
print("Number of members with scores between 120 and 200:", members_in_range_count)
# Number of members with scores between 120 and 200: 1


# Count the number of members with scores between 120 and 200(exclusive)
members_in_range_count = r.zcount('leaderboard', 120, '(200')
print("Number of members with scores between 120 and 200(exclusive):", members_in_range_count)
# Number of members with scores between 120 and 200(exclusive): 0


# Retrieve the leaderboard after removing Carol
leaderboard = r.zrange('leaderboard', 0, -1, withscores=True)
print("Leaderboard after removing Carol:", leaderboard)
# Leaderboard after removing Carol: [('Alice', 100.0), ('Bob', 200.0), ('Tom', 300.0)]


# Retrieve members from the sorted set 'leaderboard' with scores between 80 and 200
members_in_range = r.zrangebyscore('leaderboard', min=80, max=200)
print("Members in range 80-200:", members_in_range)
# Members in range 80-200: ['Alice', 'Bob']


# Retrieve members from the sorted set 'leaderboard' with scores between 80 and 200 in reverse order
members_in_range_reverse = r.zrevrangebyscore('leaderboard', min=80, max=200)
print("Members in range 80-200 (in reverse order):", members_in_range_reverse)
# Members in range 80-200 (in reverse order): ['Bob', 'Alice']


# Remove and retrieve the member with the lowest score
lowest_member = r.zpopmin('leaderboard')
print("Member with the lowest score:", lowest_member)
# Member with the lowest score: [('Alice', 100.0)]


# Remove and retrieve the member with the highest score
highest_member = r.zpopmax('leaderboard')
print("Member with the highest score:", highest_member)
# Member with the highest score: [('Tom', 300.0)]

# Increment the score of 'Bob' by 50
new_score = r.zincrby('leaderboard', 50, 'Bob')
print("New score of 'Bob':", new_score)
# New score of 'Bob': 250.0


# Increment the score of 'Dan' by 75 (creating it with an initial score of 75 if it doesn't exist)
new_score = r.zincrby('leaderboard', 75, 'Dan')
print("New score of 'Dan':", new_score)
# New score of 'Dan': 75.0


# Delete the sorted set named 'leaderboard'
r.delete('leaderboard')
