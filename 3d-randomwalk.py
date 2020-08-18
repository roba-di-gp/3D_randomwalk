import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

steps = 500    #number of steps

dev = 1   #standard deviation of the generating distribution

x, y, z = x0, y0, z0 = 0,0,0    #initial coordinates

xx, yy, zz = np.array([x0]),np.array([y0]),np.array([z0])

for n in range(0,steps):
    xstep, ystep, zstep = np.random.normal(0,dev,3)
    x = x + xstep
    xx = np.append(xx,x)
    y = y + ystep
    yy = np.append(yy,y)
    z = z + zstep
    zz = np.append(zz,z)

plt.figure(0)   #three-dimensional plot

ax = plt.axes(projection='3d')
ax.plot3D(xx,yy,zz,c='black',alpha=0.8,marker='.',markersize=3)
ax.scatter3D(x0,y0,z0,c='blue',s=20)
ax.scatter3D(xx[steps],yy[steps],zz[steps],c='red',s=20)

plt.figure(1)   #xy plane projection

plt.errorbar(xx,yy,fmt='.--',color='black')
plt.errorbar(x0,y0,fmt='.',color ='blue',markersize=15)
plt.errorbar(xx[steps],yy[steps],fmt='.',color ='red',markersize=15)
plt.title('xy projection')
plt.grid(linestyle=':')

plt.figure(2)   #yz plane projection

plt.errorbar(yy,zz,fmt='.--',color='black')
plt.errorbar(y0,z0,fmt='.',color ='blue',markersize=15)
plt.errorbar(yy[steps],zz[steps],fmt='.',color ='red',markersize=15)
plt.title('yz projection')
plt.grid(linestyle=':')

plt.figure(3)   #xz plane projection

plt.errorbar(xx,zz,fmt='.--',color='black')
plt.errorbar(x0,z0,fmt='.',color ='blue',markersize=15)
plt.errorbar(xx[steps],zz[steps],fmt='.',color ='red',markersize=15)
plt.title('xz projection')
plt.grid(linestyle=':')

plt.figure(4)

iter = np.linspace(0,steps,steps+1)

plt.subplot(311)    #x axis walk

plt.errorbar(iter,xx,color='black',fmt='.-',markersize=4)
plt.grid(linestyle=':')
plt.ylabel('x')

plt.subplot(312)    #y axis walk
   
plt.errorbar(iter,yy,color='black',fmt='.-',markersize=4)
plt.grid(linestyle=':')
plt.ylabel('y')

plt.subplot(313)    #z axis walk

plt.errorbar(iter,zz,color='black',fmt='.-',markersize=4)
plt.grid(linestyle=':')
plt.ylabel('z')
plt.xlabel('steps')

print('Starting point: \n %.1f, %.1f, %.1f \n'%(x0,y0,z0))
print('Point of arrival: \n %.1f, %.1f, %.1f \n'%(xx[steps],yy[steps],zz[steps]))
dist = np.sqrt((xx[steps]-x0)**2+(yy[steps]-y0)**2+(zz[steps]-z0)**2)
print('Final distance: \n %.3f \n'%(dist))
print('Path lenght: \n %.3f \n'%(path))

plt.show()





