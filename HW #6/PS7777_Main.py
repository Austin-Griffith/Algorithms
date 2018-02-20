import random

def resolveTiesandMin(l):
    nameList = ["Swap", "Sub", "Indel1", "Indel2"]
    #
    # print l
    ties = []
    minIndex = 0
    for i in range(0, 4): #find min
    	#print "L of ",i," is ", l[i]
        if (l[i] < l[minIndex]):
            minIndex = i
    #print minIndex
    for i in range(0,3): #
        for j in range(i,3):
             #print(i,j)
            if(j!=i and l[i]==l[j] and l[i] <= l[minIndex]):

                if(nameList[i] not in ties):
                    ties.append(nameList[i])

                if (nameList[j] not in ties):
                    ties.append(nameList[j])
    if(ties):
        if "Sub" in ties:
            return "Sub"
        else:
            randomTie = random.choice(ties)
            #print("random ",randomTie)
            return randomTie
    else:
        #print("single min= ",nameList[minIndex])
        return nameList[minIndex]


def commonSubstrings(x, L, a):
    #creates common substrings from x->y
    while(L<1 or L>len(x)):
        newl = int(input("Enter a number between 1 and " +
        str(len(x)) + "\n"))
        L = newl
	subList = list()
	substr = ""
	subchars = list()

	print(a)
	print(len(a))
	print(len(x))
	 

	 #for i in range(0,len(x)):
	 
	i=0
	while(i < len(x)):		 #compute cost by looping through s and appending correct letter to subchars
	    if (i >= len(a)):
	        i += 1
	    elif(a[i] == "NO-OP"):
	        subchars.append(x[i])
	        i += 1
	    elif(a[i] == "Swap"):
	        #a.insert(0, " ")
	        i += 2
	    else:
	        subchars.append(" ")
	        i += 1

	run = False
	for char in subchars: #append each subchar to a substring list that is used for printing the common substrings

	    if(char != " "):
	        substr = substr + char
	        if (char != subchars[-1]):
	            run = True
	        else:
				run = False
	    else:
	        if (substr != "" and len(substr) >= L):

	            subList.append(substr)
	        substr = ""

	    if (char == subchars[-1] and run == False):

	        if(substr != "" and len(substr) >= L):
				subList.append(substr)


def extractAlignment(S,x,y):
	
    #Callculates the shortest and optimal paths.
    nx = len(x)
    ny = len(y)

	i = nx 
	j = ny

    #print(len(S[0]))
	a = list()
    #print("i=",i," j=",j)

	while(i>0 or j>0):
	    #print("i=",i," j=",j, " S[i][j]=",S[i][j])
	    tieList = list()
		swap = 0 			#initialize values based on dynamic programming algorithm
		sub = 0
		indel1 = 0
		indel2 = 0

		if(i>=2 and j>=2): 		#assign values to swap, sub, indel1, indel2, based on the value of previously determined values
			swap = S[i-2][j-2]

		if (i >= 1 and j >= 1):
		    sub = S[i-1][j-1]

		if(i>=1 and j >=0):
		    indel1 = S[i - 1][j]

		if(j>=1 and i >=0):
		    indel2 = S[i][j-1]

		# if((sub == S[i][j])):
		    #a.append("NO-OP")
			# print "Q"
			# print i
			# i = i-1
			# j = j-1
		# elif(swap == sub and  sub != -1):
		   #a.append("Sub")
			# print "z"
			#print i
			# i=i-1
			# j=j-1 
		if(j <= 0):
			#print("special Indel1")
		    a.append("Indel1")
		    i = i-1
		elif(i <= 0):
		    #print("special Indel2")
		    a.append("Indel2")
		    #print a
		    j = j-1

		else:
		    tieList.append(swap)
		    tieList.append(sub)
		    tieList.append(indel1)
		    tieList.append(indel2)
		    #print("TIE LIST = ", tieList)
		    testString = resolveTiesandMin(tieList)
		    if testString is "Sub" and sub is S[i][j]: #loop through to create a which will contain the list of editsA AAAAA #check to see which string is in the test string and append that type of edit
					 a.append("NO-OP")
		    else:
		        a.append(testString)
		    if(testString == "Swap"):
		        a.append("Swap")
		        i = i-2
		        j = j-2
		    elif (testString == "Sub"):
		        i = i-1
		        j = j-1
		    elif (testString == "Indel1"):
		        i = i-1
		    elif (testString == "Indel2"):
				j = j-1

	a.reverse()
	return a			


def alignStrings(x,y):
    						#fill the matrix of optimal costs.
    nx = len(x)+1
    ny = len(y)+1
S = []

for i in range(0, nx): 		#create matrix and initialize with all
#zeroes
	new = []
	for j in range (0, ny):
    		if(i == 0):
        		new.append(j)
    		elif(j == 0):
        		new.append(i)
        	else:
            		new.append(0)
    	S.append(new)

if(x==y):
    return S

for i in range(1,nx): #actually calculates the dynamic programming table by checking the necessary previous values such as i-2,j-2 and i-1,j-1
	
	for j in range(1,ny):
	    	#print("I=",i, "J=", j)
	    	costofSub = 1
	    	costofIndel = 1
	    	costofSwap = 3

    		if(x[i-1] == y[j-1]):
				costofSub = 0

	    	if(i == 1):
	        	doSub = S[i-1][j-1] + costofSub
	        	doIndel1 = S[i-1][j] + costofIndel
	        	doIndel2 = S[i][j-1] + costofIndel
	        	costweChoose = min(doSub, doIndel1, doIndel2)
	        	#print("doSub=", doSub, " doIndel1=", doIndel1, doIndel2=", doIndel2)
	        	#print(costweChoose)

	        else:
	            doSwap = S[i-2][j-2] + costofSwap
	            doSub = S[i - 1][j - 1] + costofSub
	            doIndel1 = S[i - 1][j] + costofIndel
	            doIndel2 = S[i][j - 1] + costofIndel
	            costweChoose = min(doSwap, doSub, doIndel1,
	            doIndel2)
	            #print("doSwap=", doSwap, " doSub=", doSub, "doIndel1=", doIndel1, " doIndel2=", doIndel2)
	            #print(costweChoose)
			
	        S[i][j] = costweChoose

print "[",
print "-, ",
for c in y:
    print "c,',',"
print"]"
for i in range(len(S)):
    if(i==0):
        print"-",
    else:
        print x[i-1],
    print S[i]
return S
    
def main():

	s1 = "the white house office of the press secretary for immediate rel" 	#entire string was difficult to fit in
	s2 = "exxonmobil plans investments of $20 billion to exp"
	commonSubstrings(s1, 10, extractAlignment((alignStrings(s1,s2)), s1, s2))
	print s2
if __name__ == "__main__":
	main()            

          
                                                  









