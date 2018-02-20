# 2 people can throw at one person
# come up with more test cases for algo
# define output to terminal better



#the algorithm holds true because there are always is an odd number of ppl. 
#If there was an even case such as 4 people, then the 2 pairs of people could splash each other and therefore all ppl would be splashed
def splash(pplDistance):

	pplHit = []									#initializing an empty list for output, list of people of hit in origional order of people and distances 
	i = 0
	for i in range(len(pplDistance)):			#intializing pplHit array to all False representing that no one is initially hit
		pplHit.append(False)

	#print(pplHit)								#check to see if above loop is appending correctly


	for i in range(len(pplDistance)):			# looping through each person throwing a ballon
			minDistAt = 0						# start range at 1 bc minDistAt = 0

			for j in range(1,len(pplDistance)):			#inner loop finds the min distance to determine who person i will splash 	

					if (pplDistance[i][j] < pplDistance[i][minDistAt]):
							minDistAt = j			#updating new closest neighbor to person i

			pplHit[minDistAt] = True		# i threw a ballon at whichever person has min distance from i
			#print(pplHit)

	return(pplHit)				

 

def pplNotHit(pplHit):

	missedBallon = False		#condition for person not hit

	for i in range(len(pplHit)):		# looping through length of pplHit by index
		
		if not pplHit[i]:
			missedBallon = True
		
		print('\tperson ' + str(i) + ' was' + ( ' not' if not pplHit[i] else '' ) + ' hit' )		#output the splashed status of person i 

	if missedBallon == True:
			print('There was someone not hit by a ballon!')			#printing if someone avoided being splashed 



def main():
	
													#initialize 2D array ----> matrix of people and distance
	# pplDistance = [  [9990, 2 , 4] ,
	# 				 [2, 9990, 6], 
	# 				 [4, 6, 9990] ]       	# the distance a person between and themselves is set to a distance larger than all other distances so a person is garanteed to not splash themselves  
																		

	#test case where more than one person was not hit 
	pplDistance = [ [100, 1.3, 2, 2.5, 4],
					[1.3, 100, .7, 1.2, 2.7],
					[2, .7, 100, .5, 2],
					[2.5, 1.2, .5, 100, 1.5],
					[4, 2.7, 2, 1.5, 100]
				   ]
	 				 
	print(pplDistance)
	splashed = splash(pplDistance)		#splashed[i] is True when person i was splashed by ballon 
	
	print( str(splashed) + ":")									# at least one of the entries of splashed will be False if at least one person is not splashed 
	
	pplNotHit( splashed ) 
	
if __name__ == "__main__":
	main()







