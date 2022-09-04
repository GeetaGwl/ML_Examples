import matplotlib.pyplot as pl

ages=[5,8,9,17,19,25,66,89,43,78,22,27,96,95,11,15,19,18]

#bins=[x for x in range(0,len(ages))]

bins=[10,20,30,40,50,60,70,80,90,100]

pl.hist(ages,bins,histtype='bar',color='c',rwidth=0.7)

pl.title("interesting graph\ncheck it out")
pl.xlabel("ages")
pl.ylabel("distribution")
pl.show()
