import random
import math
reversePairCount = 0
reversePairCount1 = 0				### can get rid of this

def testCases():
	#A = [1,2,3,4,5]    #testing a no reverse pair case ----> returns 0 

	#A = [6,3,7,8,10,4]    #return 5 pairs  ----> correct 
	#A = [5,4,3,2,1]		# should return 10 pairs   -----> correct 

	#A = [7,6,5,4,3,2,1]     #cant get 21 pairs which is total count		### update that this should return 21 pairs, and does
	A = [8,7,6,5,4,3,2,1]	 # Should get 28 pairs

	print('Test case Array:')
	print(A)
	modifiedMergeSort(A)
	print(str(reversePairCount) + ' reverse pairs') 
	print('')

def countReversePairs():

															#generate random Array of 100 numbers HERE!!    below method works
	randomArray = random.sample(xrange(1, 10000), 100)
	print('Randomly genereated array:')
	print(randomArray)
	modifiedMergeSort(randomArray)

	#A = [1,2,3,4,5]    #testing a no reverse pair case ----> returns 0 			### should remove all these comments that are listed above in testCases()

	#A = [6,3,7,8,10,4]    #return 5 pairs  ----> correct 
	#A = [5,4,3,2,1]		# should return 10 pairs   -----> correct 

	#A = [7,6,5,4,3,2,1]     #cant get 21 pairs which is total count
	# A = [8,7,6,5,4,3,2,1]	 # Should get 28 pairs

	# modifiedMergeSort(A)
	print('')
	print(str(reversePairCount) + ' reverse pairs')		
	

def modifiedMergeSort(A):

	global reversePairCount				### should drop a comment saying something like "we opt to use a global pair count variable so we don't have to worry about tracking the variable through returns or parameters"

	if (len(A) == 0 or len(A) == 1 ):		#base case		### could mention that "in this case there are no reverse pairs because no elements are being compared yet"
		return A 
		
	#splitIndex = math.floor(len(A)/2)    ----> possible case 		### can remove this
	
	splitIndex = ( len(A) / 2 )			#split array by length
	left = A[0:splitIndex]
	right = A[splitIndex:len(A)]


	leftSorted = modifiedMergeSort(left)
	rightSorted = modifiedMergeSort(right)

	sortedCombine = []			### can add comment saying "now that we have two sorted arrays, we merge them"
	
	while (len(leftSorted) > 0 or len(rightSorted) > 0):

		if (len(leftSorted) == 0):		### could add comment that in this case there are no reverse pairs because the left array is empty
			sortedCombine.append(rightSorted[0])			#no values in leftSorted so appends first value in rightSorted to Combine array
			rightSorted = rightSorted[1:len(rightSorted)]

		elif(len(rightSorted) == 0 ):
			sortedCombine.append(leftSorted[0])				#no values in rightSorted so appends first value in leftSorted to Combine array
			leftSorted = leftSorted[1:len(leftSorted)]		#strips that value added to Combine array

		elif(leftSorted[0] > rightSorted[0]):			#pull from right and then increase the amount of reversePairs by amount left in leftSorted 
			sortedCombine.append(rightSorted[0])
			rightSorted = rightSorted[1:len(rightSorted)]	#strips that value added to Combine array		### maybe add "from rightSorted"
			reversePairCount += len(leftSorted)				#counts all pairs		### could add that additionally, we know this is the number of reverse pairs because pulling from the right array means it is before every element in leftSorted because rightSorted[0] < leftSorted[0] and leftSorted[0] <= leftSorted[1] <= leftSorted[2]...

		else:	
			sortedCombine.append(leftSorted[0])
			leftSorted = leftSorted[1:len(rightSorted)]
														# no need to increment reversePairs bc left side is already less than everything on right side
														###                                        ^leftSorted[0]              ^ or equal to 
														### maybe rephrase that there are no reverse pairs here because leftSorted[0] <= everything in rightSorted
														### also move this comment up a couple lines, maybe on the same line as the else
	return sortedCombine 		### could leave a comment saying that we now return a sorted array that has merged leftSorted and rightSorted

######################################## END OF PROBLEM 1 IMPLEMENTATION ########################################################################	


######################################## START OF PROBLEM 2 IMPLEMENTATION ########################################################################	










######################################## END OF PROBLEM 2 IMPLEMENTATION ########################################################################	


######################################## START OF PROBLEM 4 IMPLEMENTATION ########################################################################	


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
																		### maybe say, to confirm that our findPaths implementation works, we get the result directly via networkx



def findPaths(G,v):				#function will take in a graph and a starting vertex as parameters 
								# this function will count total paths from a given vertex to sink for any vertex in the graph 

								
	pathCount = 0				# variable to count number of paths from source to sink 
																	###    ^ should be "from v to sink"
	if (v == "Fly"):			# base case  --->. checking to see Fly is passed in ---> Fly only has one path to itself 
		#print("made it")
		return 1
		
	for vertex in [ i for i in G[ v ].keys() ]:		# loop iterates over all possible nodes that vertex is connected to		### itterates -> iterates; also maybe change vertex to v
		
		#print(G[ v ])
		pathCount += findPaths( G, vertex)			# pathCount gets incremented by the number of paths from vertex to sink of graph 		### incredemented -> incremented; maybe change vertex to v
													### can also add on that the number of paths from v to sink is equal to the sum of the number of paths from each adjacent vertex to sink, as v can get to any adjacent vertex

	#print(pathCount)			### just remove all the prints that are commented out, so this one and the two above
	return pathCount	


############################################### END OF PROBLEM 4 IMPLEMENTATION ########################################################################	


############################################### START OF PROBLEM 5 IMPLEMENTATION ########################################################################	
# 2 people can throw at one person
# come up with more test cases for algo
# define output to terminal better



#the algorithm holds true because there are always is an odd number of ppl. ### rephrase as "there is always an odd number of people"
#If there was an even case such as 4 people, then the 2 pairs of people could splash each other and therefore all ppl would be splashed
def splash(pplDistance):

	pplHit = []									#initializing an empty list for output, list of people of hit in origional order of people and distances 
	i = 0
	for i in range(len(pplDistance)):			#intializing pplHit array to all False representing that no one is initially hit
		pplHit.append(False)

	#print(pplHit)								#check to see if above loop is appending correctly ### or just remove this line


	for i in range(len(pplDistance)):			# looping through each person throwing a ballon
			minDistAt = 0						# start range at 1 bc minDistAt = 0			### maybe rephrase as "start by assuming person 0 splashes person i"

			for j in range(1,len(pplDistance)):			#inner loop finds the min distance to determine who person i will splash

					if (pplDistance[i][j] < pplDistance[i][minDistAt]):
							minDistAt = j			#updating new closest neighbor to person i

			pplHit[minDistAt] = True		# i threw a ballon at whichever person has min distance from i		### maybe tack on "has min distance from i -- person j"
			#print(pplHit)			### can remove this

	return(pplHit)				

 

def pplNotHit(pplHit):

	missedBallon = False		#condition for person not hit			### maybe rename this "unHit" or "escapedHit" or "someoneUnsplashed"

	for i in range(len(pplHit)):		# looping through length of pplHit by index
		
		if not pplHit[i]:
			missedBallon = True
		
		print('\tperson ' + str(i) + ' was' + ( ' not' if not pplHit[i] else '' ) + ' hit' )		#output the splashed status of person i 

	if missedBallon == True:
			print('There was someone not hit by a ballon!')			#printing if someone avoided being splashed 



############################################### END OF PROBLEM 5 IMPLEMENTATION ########################################################################	



def main():
	
	reversePairCount = 0    #used for problem 1

	print("")
	testCases()
	print('')
	countReversePairs()				#call to problem 1 
	print("")


	print("Total paths in the graph =")
	print( findPaths(G,"Spider") )																	#call to problem 4 	# prints total paths Spider to Fly  ----> 141 
	if (findPaths(G,"Spider") == len( [i for i in nx.all_simple_paths(G,"Spider","Fly") ] )):		#trivial solution using NextworkX feature....if condition holds true so found all paths
		print("Success! My solution matches trivial solution")
	print("")

	#initialize 2D array ----> matrix of people and distance
	# pplDistance = [  [9990, 2 , 4] ,
	# 				 [2, 9990, 6], 
	# 				 [4, 6, 9990] ]       	# the distance a person between and themselves is set to a distance larger than all other distances so a person is garanteed to not splash themselves  
																		

	#test case where more than one person was not hit 
	pplDistance = [ [100, 1.3, 2, 2.5, 4],			### maybe add comment that pplDistance[i][j] is the distance between person i and person j
					[1.3, 100, .7, 1.2, 2.7],
					[2, .7, 100, .5, 2],
					[2.5, 1.2, .5, 100, 1.5],
					[4, 2.7, 2, 1.5, 100]
				   ]
	 				 
	print(pplDistance)
	splashed = splash(pplDistance)		#splashed[i] is True when person i was splashed by ballon 
	
	print( str(splashed) + ":")									# at least one of the entries of splashed will be False if at least one person is not splashed 
	
	pplNotHit( splashed ) 
	

	print("")
	
	
	
if __name__ == "__main__":
	main()










