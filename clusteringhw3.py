
from math import sqrt
import os

#updates the new centroid of given cluster
def updateCentroid(cenList):
    x=0
    y=0
    if len(cenList) == 1:
        return (cenList[0][0],cenList[0][1])
    else:
        for i in cenList:
            x += i[0]
            y += i[1]
        return( ( x/len(cenList), y/len(cenList) ) )

os.system('cls')
table1 = [(2,10),(2,5),(8,4),(5,8),(7,5),(6,4),(1,2),(4,9)]
iteration = 0
stop = False

centroid1old = (1,1)
centroid2old = (4,4)
centroid3old = (7,7)

centroid1new = (0,0)
centroid2new = (0,0)
centroid3new = (0,0)

#list to store distance
dist = [0,0,0]

#closest point index
closest = 0

while (not stop == True):
    iteration += 1
    #lists to see which points belong to which centroid
    cenList1 = []
    cenList2 = []
    cenList3 = []

    for i in table1:
        #compute distance of point to each centroid
        dist[0] = sqrt( ((i[0]-centroid1old[0])**2) + ((i[1]-centroid1old[1])**2) )
        dist[1] = sqrt( ((i[0]-centroid2old[0])**2) + ((i[1]-centroid2old[1])**2) )
        dist[2] = sqrt( ((i[0]-centroid3old[0])**2) + ((i[1]-centroid3old[1])**2) )

        #choose only the smallest distance
        closest = dist.index(min(dist))

        if closest == 0:
            cenList1.append(i)
            
        if closest == 1:
            cenList2.append(i)
            
        if closest == 2:
            cenList3.append(i)
    
    #Update the new centroid of the new cluster
    centroid1new = updateCentroid(cenList1)
    centroid2new = updateCentroid(cenList2)
    centroid3new = updateCentroid(cenList3)

    print(centroid1new, centroid1old)
    print(centroid2new, centroid2old)
    print(centroid3new, centroid3old)
    print('---------')

    #check to see if the new centroids are equal to the old centroids
    #if they are equal, then we have achieved convergence and break the while loop
    if ((centroid1new == centroid1old) and (centroid2new == centroid2old)) and centroid3new == centroid3old:
        stop = True
    else:
        centroid1old = centroid1new
        centroid2old = centroid2new
        centroid3old = centroid3new


print()
print(cenList1)
print(cenList2)
print(cenList3)
print()
print(centroid1new)
print(centroid2new)
print(centroid3new)


