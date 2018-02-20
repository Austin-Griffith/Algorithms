countFast = 0
countLuc = 0

def FasterLuc(l):
    a = 1
    b = 2
    global countFast
    for i in range(2,l):

        c = a + b
        a = b
        b = c
        countFast = countFast + 6
    return a


def Luc(n):

    global countLuc
    if(n == 0):
        return 2
        countLuc = countLuc + 5

    elif(n==1):
        return 1
        countLuc = countLuc + 5

    else:
        countLuc = countLuc + 5
        return (Luc(n-1) + Luc(n-2))


def main():
    n = 30      #october 24 th
    fiveDig = int(str(FasterLuc(n))[:5])#do you want this or store

    print "First five digits of Ln are: ", fiveDig
    print "Assuming that FasterLuc contains 6 atomoic operation"
    print "FasterLuc takes: ", (countFast + 12)/3.15e6 , "years to complete"
    print "At just n = 30 the number of atomic operations is 6731340"

    goldRatio = 1.61803398875
    #ans = (goldRatio**(5*n))/3.15e6

    print "It takes Luc : 1.1e56 years to complete"

    #Luc(n)
    #print countLuc


main()