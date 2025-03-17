import redis
from redisgraph import Graph, Node, Edge

# Establish connection to Redis
r = redis.Redis(host='redis-graph', port=6379, db=0, decode_responses=True)

# # Delete if there is
# r.delete('social')

# Initialize a RedisGraph named 'social'
graph = Graph('social', r)

# Create nodes
john = Node(label='person', properties={'name': 'John', 'age': 35})
jane = Node(label='person', properties={'name': 'Jane', 'age': 32})

# Add nodes to the graph
graph.add_node(john)
graph.add_node(jane)

# Create an edge (relationship) between the nodes
friendship = Edge(john, 'FRIEND', jane, properties={'since': '2021'})

# Add the edge to the graph
graph.add_edge(friendship)

# Commit the changes to the database
graph.commit()

# Query: find friends of John
query = """MATCH (john:person)-[:FRIEND]->(friend:person)
           WHERE john.name = 'John'
           RETURN friend.name, friend.age"""

# Execute the query
result = graph.query(query)

# Print the results
print("John's friends:")
for record in result.result_set:
    print(f"Name: {record[0]}, Age: {record[1]}")