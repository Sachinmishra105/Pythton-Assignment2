# write a python program to get a list,sorted in increasing order by the last element in each tuple from a given list
#  of non empty tuples.



x = [(2,5),(1,2),(4,4),(2,3),(2,1)]
print("List of tuples before sorting: " + str(x))

last = len(x)
for i in range(0,last):
    for j in range(0,last-i-1):
        if( x[j][-1] > x[j + 1][-1]):
            swap = x[j]
            x[j] = x[j + 1]
            x[j + 1] = swap            
print("List of tuple after sorting : " + str(x))




