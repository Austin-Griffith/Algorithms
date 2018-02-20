import random
import math
reversePairCount = 0
 

def testCases():
	#A = [1,2,3,4,5]    #testing a no reverse pair case ----> returns 0 

	#A = [6,3,7,8,10,4]    #return 5 pairs  ----> correct 
	#A = [5,4,3,2,1]		# should return 10 pairs   -----> correct 

	#A = [7,6,5,4,3,2,1]     #cant get 21 pairs which is total count
	A = [8,7,6,5,4,3,2,1]	 # Should get 28 pairs

	print('Test case Array:')
	print(A)
	modifiedMergeSort(A)
	print(reversePairCount,'reverse pairs') 
	print('')

def countReversePairs():

															#generate random Array of 100 numbers HERE!!    below method works
	randomArray = random.sample(xrange(1, 10000), 100)
	print('Randomly genereated array:')
	print(randomArray)
	modifiedMergeSort(randomArray)

	print('')
	print(reversePairCount,'reverse pairs')
	

def modifiedMergeSort(A):

	global reversePairCount

	if (len(A) == 0 or len(A) == 1 ):		#base case
		return A 
		
	#splitIndex = math.floor(len(A)/2)    ----> possible case 
	
	splitIndex = ( len(A) / 2 )			#split array by length
	left = A[0:splitIndex]
	right = A[splitIndex:len(A)]


	leftSorted = modifiedMergeSort(left)
	rightSorted = modifiedMergeSort(right)

	sortedCombine = []
	
	while (len(leftSorted) > 0 or len(rightSorted) > 0):

		if (len(leftSorted) == 0):
			sortedCombine.append(rightSorted[0])			#no values in leftSorted so appends first value in rightSorted to Combine array
			rightSorted = rightSorted[1:len(rightSorted)]

		elif(len(rightSorted) == 0 ):
			sortedCombine.append(leftSorted[0])				#no values in rightSorted so appends first value in leftSorted to Combine array
			leftSorted = leftSorted[1:len(leftSorted)]		#strips that value added to Combine array


		elif(leftSorted[0] > rightSorted[0]):			#pull from right and then increase the amount of reversePairs by amount left in leftSorted 
			sortedCombine.append(rightSorted[0])
			rightSorted = rightSorted[1:len(rightSorted)]	#strips that value added to Combine array
			reversePairCount += len(leftSorted)				#counts all pairs

		else:	
			sortedCombine.append(leftSorted[0])
			leftSorted = leftSorted[1:len(rightSorted)]
														# no need to increment reversePairs bc left side is already less than everything on right side 

	return sortedCombine 

######################################## END OF PROBLEM 1 IMPLEMENTATION ########################################################################	

def main():
	
	reversePairCount = 0    #used for problem 1
	testCases()
	countReversePairs()		#call to problem 1 
	
	
	
if __name__ == "__main__":
	main()

