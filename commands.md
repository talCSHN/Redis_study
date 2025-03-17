# SET
127.0.0.1:6379> SET mykey "Hello"
OK

# SET with expiration
127.0.0.1:6379> SET mykey 15 EX 3
OK

# GET
127.0.0.1:6379> GET mykey
"Hello"

# HSET
127.0.0.1:6379> HSET user name Joon username mke age 30
(integer) 3

# HSET nested hash(not official)
127.0.0.1:6379> HSET user:address street "123 Main St" city "Anytown" zip "12345"
(integer) 3

# HGET
127.0.0.1:6379> HGET user name
"Joon"

# HGETALL
127.0.0.1:6379> HGETALL user
1) "name"
2) "Joon"
3) "username"
4) "mke"
5) "age"
6) "30"

# HEXISTS
127.0.0.1:6379> HEXISTS user name
(integer) 1
127.0.0.1:6379> HEXISTS user gender
(integer) 0

# DEL
127.0.0.1:6379> DEL user
(integer) 1

# HDEL
127.0.0.1:6379> HDEL user name
(integer) 1
127.0.0.1:6379> HGETALL user
1) "username"
2) "mke"
3) "age"
4) "30"

# HINCRBY
127.0.0.1:6379> HINCRBY user age 1
(integer) 31
127.0.0.1:6379> HGET user age
"31"
127.0.0.1:6379> HINCRBY user age -1
(integer) 30

# HINCRBYFLOAT
127.0.0.1:6379> HINCRBYFLOAT user age 1.1
"32.1"

# HSTRLEN(where username is mke)
127.0.0.1:6379> HSTRLEN user username
(integer) 3

# HKEYS
127.0.0.1:6379> HKEYS user
1) "username"
2) "age"

# HVALS
127.0.0.1:6379> HVALS user
1) "mke"
2) "30"
