def abc(*args):
    print(args[0][0])
def abc2(**kwargs):
    print(kwargs)  

l=[1,2,3,4]
abc(l)  

d={"name":"aaa","age":20}
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
 
# Driver code
myFun(x="first",b="sec",c="thrid")   