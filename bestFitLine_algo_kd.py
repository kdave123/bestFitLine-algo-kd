#bestFitLine_Kd
#recursive midpoints line

import matplotlib.pyplot as plt
import numpy as np
x = [1,2,4,6,7,8,9,11,14,16,18,22,25,26]
y = [1,5,3,8,5,10,4,14,9,16,11,18,15,24]
x = np.array(x);
y = np.array(y);

print(x);
print(y);

plt.plot(x,y,'o')

def makeline(x,y):
    newx = np.array([])
    newy = np.array([])
    for i in range(0, len(x) - 1):

        midx = ((x[i] + x[i + 1]) / 2)
        midy = ((y[i] + y[i + 1]) / 2)
        newx = np.append(newx, midx)
        newy = np.append(newy, midy)
    # Keep calculating mid-points of points and join midpoints, loopover. untill only 2 points are left in array
    if (len(newx) > 2):
        newx, newy = makeline(newx, newy)
    return newx,newy
newx,newy =makeline(x,y)

print("bestfitline x1 x2 y1 y2")
print(newx,newy)
slope= (newy[1]-newy[0])/(newx[1]-newx[0])
print("slope")
print(slope)
plt.plot(newx,newy)
print("y-intercept")
print(-((slope*newx[0])-newy[0]))
plt.show()