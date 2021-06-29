a, b = 0, 0
edges = []
count_of_edges = int(input())
for i in range(count_of_edges):
	# edges.append((i, (i+2)%3))
	edges.append((int(input()), int(input())))

print(edges)
edges = sorted(edges, key = lambda x: x[1])
print(edges)

result = []
last_edge = (0, 0)
for edge in edges:
	if not(result) or edge[0] >= result[-1][1]:
		result.append(edge)

print(f"result: {result}\nlen: {len(result)}") 