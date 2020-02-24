import numpy as np
from sympy import*

n = 10
xinit = np.linspace(-2,2,n)
xp = np.linspace(-2,2,100)
yrealf = []
yp = []
masterlist = []
xp1 = []
xp2 = []
yp1 = []
yp2 = []
#Create main function for the equation provided in the question
def mainfunc(x):
    y = np.exp(x)+2**(-x)+2*(np.cos(x))-6
    return y

#Declare lists for all the variables required for computing the coefficients
a = []
b = []
c = []
d = []
h = []
alpha = ["nil"]

for i in range(len(xinit)):
    a.insert(i, mainfunc(xinit[i]))

for i in range(0,n-1):
    h.insert(i,xinit[i+1]-xinit[i])

for i in range(1,n-1):
    alpha.insert(i, 3*(((a[i+1]-a[i])/h[i])-((a[i]-a[i-1])/h[i-1])))

i00 = [0]
z = [0]
mu = [0]

for i in range(1,n-1):
    i00.insert(i,2*(xinit[i+1]-xinit[i-1])-((h[i-1])*(mu[i-1])))
    mu.insert(i,h[i]/i00[i])
    z.insert(i,(alpha[i]-(h[i-1]*z[i-1]))/i00[i])
    
i00.insert(n-1,1)
z.insert(n-1,0)

for i in range(n):
    c.insert(i,0)
    b.insert(i,0)
    d.insert(i,0)

j = n-2
while(j>=0):
    c[j]=z[j]-(mu[j]*c[j+1])
    b[j]=((a[j+1]-a[j])/h[j])-(h[j]*(c[j+1]+2*c[j]))/3
    d[j]=(c[j+1]-c[j])/(3*h[j])
    j = j-1

#Remove last values of each list as they are not used in the calculation
a.pop(n-1)
b.pop(n-1)
c.pop(n-1)
d.pop(n-1)

for i in range(len(xp)):
    yrealf.insert(i, mainfunc(xp[i]))

#Cubic Spline Loop
for i in range(len(xp)):
    for j in range(n-1):
        if(xinit[j]<=xp[i] and xp[i]<xinit[j+1]):
            yp.insert(i,(a[j]+(b[j]*(xp[i]-xinit[j]))+(c[j]*((xp[i]-xinit[j])**2))+(d[j]*((xp[i]-xinit[j])**3))))
            masterlist.insert(i,(xp[i],yp[i],j))
            #print("x: "+str(xp[i])+", y: "+str(yp[i])+", j:"+str(j)+", i:"+str(i))
        if(xp[i]==xinit[n-1]):
            yp.insert(i,(a[n-2]+(b[n-2]*(xp[i]-xinit[n-2]))+(c[n-2]*((xp[i]-xinit[n-2])**2))+(d[n-2]*((xp[i]-xinit[n-2])**3))))
            masterlist.insert(i,(xp[i],yp[i],j))
            break

for i in range(len(masterlist)):
    if(masterlist[i][2]%2==0):
        xp1.append(masterlist[i][0])
        yp1.append(masterlist[i][1])
    if(masterlist[i][2]%2!=0):
        xp2.append(masterlist[i][0])
        yp2.append(masterlist[i][1])
    
#for i in range(len(a)):
    #print("a"+str(i)+":" +"%.5f" % a[i]+" b"+str(i)+":"+"%.5f" % b[i]+" c"+str(i)+":" +"%.5f" % c[i]+" d"+str(i)+":" +"%.5f" % d[i])

