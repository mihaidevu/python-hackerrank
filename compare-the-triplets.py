a = [5, 6, 7]
b = [3, 6, 10]

def compareTriplets(a, b):
    alice = bob = 0
    for x in range(3):
        if a[x] > b[x]:
            alice += 1
        elif a[x] < b[x]:
            bob +=1
    return(alice, bob)

compareTriplets(a, b)

#Pythonic way
