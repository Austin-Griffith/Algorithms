import random
import string
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

def getDictIndex(char):		
	
	aDict={"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}	
	#print aDict.get(char)	

def hash_funtion():
	
	l = 5701
	file = open("hashingList.txt","r+")
	nameSize = 0
	names = []
	index = 0


	for line in file:      		 #loop to get names from text file into single list of only names
		fields = line.split()
		names.append(fields[0])
		nameSize += 1


	randomlySelectedNames = []			#empty array to store randomly selected names
	#print(halfOfList)
	#print(len(names))
	#print(nameSize)          #print statement to check if loop is working for list of names
	

	for i in range(0,nameSize-1):
		index = random.randint(0,nameSize-1)			#selects random int between 0 and halflist
		#print(index)	
		if names[index] not in randomlySelectedNames:	
				randomlySelectedNames.append(names[index])
									

	randomNames = randomlySelectedNames[:len(randomlySelectedNames)/2]
	#print(randomlySelectedNames, "    ")
	#print(len(names))
	#print("test")	

	hash1 = []			#empty array for hash 1 and 2
	hash2 = []			
	A = ord('A')		#set variable A to the ACSII value of A

	for name in randomNames:			#looping through random names
		x = 0
		for i in name:							#looping through each letter of name
				if 'A' <= i <= 'Z':				#condition to check if each letter in name is within given ASCII vales A --> Z
					x += ord(i) - A + 1 	
		hash1.append(x % l)

	print(hash1)

	for name in randomNames:
		x = 0
		for i in name:
				if 'A' <= i <= 'Z':
					x += ord(i) - A + 1
				
		hash2.append( (x * random.randint(0,l) ) % l )

	print(hash2)


	############CREATE HISTOGRAMS (2b)##########


	n, bins, patches = plt.hist(hash1, 500)
	plt.xlabel('Hash Key Value')
	plt.ylabel('Collisions')
	plt.title(r'Histogram of first hash function')
	plt.show()

	n, bins, patches = plt.hist(hash2, 200)
	plt.xlabel('Hash Key Value')
	plt.ylabel('Collisions')
	plt.title(r'Histogram of second hash function')
	plt.show()


	############CREATE PLOTS (2d)###############

	n = 1
	temp1dFirst = []
	temp1dSecond = []
	yfirstHash = []
	ysecondHash = []
	x = []
	while n < 2000:
		x.append(n)
		n = n + 1
		temp1dFirst = hash1[:n]
		temp1dSecond = hash2[:n]
		yfirstHash.append(temp1dFirst.count(max(set(temp1dFirst), key=temp1dFirst.count)))
	 	ysecondHash.append(temp1dSecond.count(max(set(temp1dSecond), key=temp1dSecond.count)))

	plt.scatter(x,yfirstHash)
	plt.xlim(0,1500)
	plt.title('Collisions vs Input Size with hash 1')
	plt.xlabel('Input Size')
	plt.ylabel('# of Collisions')
	plt.show()

	plt.scatter(x,ysecondHash)
	plt.xlim(0,1500)
	plt.title('Collisions vs Input Size with hash 2')
	plt.xlabel('Input Size')
	plt.ylabel('# of Collisions')
	plt.show()

						
	file.close()

	return 		


def main():
	
	hash_funtion()

main()	


