import numpy as np
from sympy import*

n = 10
xinit = np.linspace(-2,2,n)

#Create main function for the equation provided in the question
def mainfunc(x):
    y = np.exp(x)+2**(-x)+2*(np.cos(x))-6
    return y
yinit = np.array ([mainfunc(i) for i in xinit])

#Create Lagrange Function
def lagrange (x, i, xinit):
    n = len(xinit)-1
    y=1

    for j in range(n+1):
        if i!=j:
            y*=(x-xinit[j])/(xinit[i]-xinit[j])
    return y

#Fill values from the Lagrange polynomial
def fillvalues (x, xinit, yinit):
    y00 = np.array ([lagrange (x, i, xinit) for i in range (n)])
    y = np.dot(yinit, y00)
    return y

xp = np.linspace (-2,2,100)
yp = fillvalues (xp,xinit,yinit)

#Divided Difference Section
NewtonDividedDifference = []
for i in range(n):
    NewtonDividedDifference.insert(n,[])
    NewtonDividedDifference[i].insert(0,yinit[i])
    
for i in range(1,n):
    for j in range(1,i+1):
        NewtonDividedDifference[i].insert(j,((NewtonDividedDifference[i][j-1]-NewtonDividedDifference[i-1][j-1])/(xinit[i]-xinit[i-j])))
        
file = open("DividedDiff.txt","w+")
for i in range(n):
    file.write("i : "+str(i)+" | ")
    for j in range(i+1):
        if(NewtonDividedDifference[i][j] > 0):
            file.write(" "+"%.5f" % NewtonDividedDifference[i][j]+"  | ")
        if(NewtonDividedDifference[i][j] < 0):
            file.write(""+"%.5f" % NewtonDividedDifference[i][j]+"  | ")
    file.write("\n")
file.close()
