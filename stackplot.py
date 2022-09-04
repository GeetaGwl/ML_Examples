import matplotlib.pyplot as pl

days=[1,2,3,4,5]

sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]


pl.plot([],[],label='sleeping',linewidth=3)
pl.plot([],[],label='eating',linewidth=3)
pl.plot([],[],label='working',linewidth=3)
pl.plot([],[],label='playing',linewidth=3)

pl.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','b'])
# in this function 1st parameter is X-axis and remaining are Y-axis

pl.xlabel("Days")
pl.ylabel("Activities")

pl.legend()

pl.show()
