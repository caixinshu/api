# coding=utf-8

def findSmallest(arr):
	samlllest = arr[0]
	samlllest_index = 0
	for i in range(1,len(arr)):
		samlllest = arr[i]
		samlllest_index = i
	return samlllest_index


def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		samlllest = findSmallest(arr)
		newArr.append(arr.pop(samlllest))
	return newArr

def countdown(i):
	print i
	if i <= 0:
		return
	else:
		countdown(i-1)

def quicksort(array):
	if len(array)<2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		
		greater = [i for i in array[1:] if i > pivot]
		
		return quicksort(less) + [pivot] + quicksort(greater)

graph = {}
graph['you'] = ['alice','bob','claire']
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] =3
graph['b']['fin']=5
graph['fin']={}

infinity = float('inf')
costs = {}
costs['a']=6
costs['b']=2
costs['fin']=infinity

parents = {}
parents['a']="start"
parents['b']="start"
parents['fin']=None

processed=[]
def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)

fruits = set(["avocado","tomato","banana"])
vegetables = set(["beets","carrots","tomato","banana"])
print fruits-vegetables