#/usr/bin/env python3
graph = {
	1:[2,3,4],
	2:[5,6],
	5:[9,10],
	4:[7,8],
	7:[11,12],
}

def bfs(graph, start, end):
	que = []
	que.append([start])
	while que:
		path = que.pop(0)
		node = path[-1]
		if node == end:
			return path
		for adjacent in graph.get(node, []):
			new_path = list(path)
			new_path.append(adjacent)
			que.append(new_path)
			#print(que,'____',path)
		#print(que,'----------------------',path)

print(bfs(graph, 1, 11))

