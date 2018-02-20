
import networkx as nx

#creates a directed graph
G = nx.DiGraph()

#adding an edge also adds the node
G.add_edge('Spider', 'A', weight=1.0)
G.add_edge('Spider', 'H', weight=1.0)
G.add_edge('Spider', 'J', weight=1.0)

G.add_edge('H', 'G', weight=1.0)
G.add_edge('H', 'K', weight=1.0)

G.add_edge('G', 'L', weight=1.0)
G.add_edge('G', 'F', weight=1.0)

G.add_edge('F', 'E', weight=1.0)

G.add_edge('E', 'Fly', weight=1.0)

G.add_edge('J', 'S', weight=1.0)
G.add_edge('J', 'K', weight=1.0)

G.add_edge('K', 'L', weight=1.0)
G.add_edge('L', 'M', weight=1.0)
G.add_edge('M', 'N', weight=1.0)
G.add_edge('M', 'F', weight=1.0)

G.add_edge('N', 'O', weight=1.0)
G.add_edge('N', 'E', weight=1.0)

G.add_edge('O', 'Fly', weight=1.0)

G.add_edge('A', 'S', weight=1.0)
G.add_edge('A', 'B', weight=1.0)

G.add_edge('B', 'R', weight=1.0)
G.add_edge('B', 'C', weight=1.0)

G.add_edge('S', 'R', weight=1.0)
G.add_edge('R', 'Q', weight=1.0)

G.add_edge('Q', 'C', weight=1.0)
G.add_edge('Q', 'P', weight=1.0)

G.add_edge('C', 'D', weight=1.0)
G.add_edge('D', 'Fly', weight=1.0)
G.add_edge('P', 'D', weight=1.0)
G.add_edge('P', 'O', weight=1.0)
G.add_edge('O', 'Fly', weight=1.0)

G.add_edge('T', 'Q', weight=1.0)
G.add_edge('T', 'P', weight=1.0)
G.add_edge('T', 'O', weight=1.0)
G.add_edge('T', 'N', weight=1.0)
G.add_edge('T', 'M', weight=1.0)

G.add_edge('R', 'T', weight=1.0)
G.add_edge('S', 'T', weight=1.0)
G.add_edge('J', 'T', weight=1.0)
G.add_edge('K', 'T', weight=1.0)
G.add_edge('L', 'T', weight=1.0)



#print(len( [i for i in nx.all_simple_paths(G,"Spider","Fly") ] ) )		#trivial answer  ----> returns 141 total paths from source to destination 



def findPaths(G,v):				#function will take in a graph and a start vertex as parameters 
								# this function will count total paths from a given vertex to sink for any vertex in the graph 

								
	pathCount = 0				# variable to count number of paths from source to sink 
	if (v == "Fly"):			# base case  --->. checking to see Fly is passed in ---> Fly only has one path to itself 
		#print("made it")
		return 1
		
	for vertex in [ i for i in G[ v ].keys() ]:		# loop itterates over all possible nodes that vertex is connected to
		
		#print(G[ v ])
		pathCount += findPaths( G, vertex)			# pathCount gets incredemented by the number of paths from vertex to sink of graph 

	#print(pathCount)	
	return pathCount	





def main():
	
	print( findPaths(G,"Spider") )				# prints total paths Spider to Fly  ----> 141 

	if (findPaths(G,"Spider") == len( [i for i in nx.all_simple_paths(G,"Spider","Fly") ] )):
		print("Success!")

	
if __name__ == "__main__":
	main()











