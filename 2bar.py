import matplotlib.pyplot as pl

x=[1,2,3,4,5]
y=[6,7,8,2,4]

x2=[1,2,3,4,5]
y2=[7,8,2,4,2]

pl.bar(x,y,label='first line',color='r',width=0.3)
pl.bar(x2,y2,label='second line',color='g',width=0.3)

pl.title("interesting graph\ncheck it out")
pl.xlabel("plot number")
pl.ylabel("importent var")
pl.legend()
pl.show()
