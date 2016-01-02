def findshortestPath(graph,start,end,path=[]):

	path = path + [start]

	if start == end:
		return path
	if start not in graph.keys():
		return None

	shortestPath = None
	for node in graph[start]:
		if node not in path:
			newPath = findshortestPath(graph,node,end,path)

			if not shortestPath or len(newPath) < shortestPath:
				shortestPath = newPath
	return shortestPath


def topologicalSort(graph):
	result = []

	while graph:
		acyclic = False

		for node,edges in graph.items():
			for edge in edges:
				if edge in graph:
					break
			else:
			   	acyclic = True
			   	del graph[node]
			   	result.append(node)
        if not acyclic:
	        print 'graph has a cycle!'
	return result



#graph = {'A': ['B', 'C'],'B': ['C', 'D'],'C': ['D'], 'D': ['C'],'E': ['F'],'F': ['C']}

graph = {2: [], 5: [11],  11: [2,9,10], 7: [11,8] , 9: [],10: [], 8 : [9], 3 : [10,8] }
#print findshortestPath(graph, 'A', 'D')
print topologicalSort(graph)