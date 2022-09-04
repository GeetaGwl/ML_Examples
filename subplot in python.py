import random
import matplotlib.pyplot as pl
from matplotlib import style

style.use("fivethirtyeight")

fig=pl.figure()

def create_plots():
    xs=[]
    ys=[]
    for i in range(10):
        x=i
        y=random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs,ys

ax1=pl.subplot2grid((4,2),(0,0),rowspan=1,colspan=1)
ax2=pl.subplot2grid((4,2),(0,1),rowspan=1,colspan=1)
ax3=pl.subplot2grid((4,2),(2,0),rowspan=1,colspan=1)
ax4=pl.subplot2grid((4,2),(2,1),rowspan=1,colspan=1)


'''
##method 1
## first parameter is height,second is width and third is plot number

ax1=fig.add_subplot(211)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax4=fig.add_subplot(224)
'''
x,y=create_plots()
ax1.plot(x,y)

x,y=create_plots()
ax2.plot(x,y)

x,y=create_plots()
ax3.plot(x,y)

x,y=create_plots()
ax4.plot(x,y)

pl.show()         
