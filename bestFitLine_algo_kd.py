#bestFitLine_Kd
#recursive midpoints line

import matplotlib.pyplot as plt
import numpy as np


#sorted x train
#ogx = [1,2,8,9,11,14,16,18,22,25,26]
#ogy = [1,5.29,10,4,14,9,16,11,18,15,24]

#unsorted x train
#ogx = [26,2,25,16,9,14,11,8,18,22,1]
#ogy = [24,5,15,16,4,9,14,10,11,18,1]

ogx = [26,2,4,25,7,16,9,14,11,8,18,22,6,1]
ogy = [24,5,3,15,5,16,4,9,14,10,11,18,8,1]
#Add funtion for repeated x train values

#Sorting data as per x train
ogx,ogy = zip(*sorted(zip(ogx,ogy)))

ogx = np.array(ogx);
ogy = np.array(ogy);

print(ogx);
print(ogy);


def makeline(x,y):
    newx = np.array([])
    newy = np.array([])
    for i in range(0, len(x) - 1):

        midx = ((x[i] + x[i + 1]) / 2)
        midy = ((y[i] + y[i + 1]) / 2)
        newx = np.append(newx, midx)
        newy = np.append(newy, midy)
        #plt.plot([x[i],x[i+1]],[y[i],y[i+1]],'r')
    #plt.plot(ogx, ogy, 'o')
    #plt.plot(newx, newy)
    #plt.show()
    # Keep calculating mid-points of points and join midpoints, loopover. untill only 2 points are left in array
    if (len(newx) > 2):
        newx, newy = makeline(newx, newy)
    return newx,newy
newx,newy =makeline(ogx,ogy)

print("bestfitline x1 x2 y1 y2")
print(newx,newy)
slope= (newy[1]-newy[0])/(newx[1]-newx[0])
print("slope")
print(slope)
plt.plot(newx,newy,'b')
print("y-intercept")
print(-((slope*newx[0])-newy[0]))
plt.plot(ogx, ogy, 'o')

plt.show()