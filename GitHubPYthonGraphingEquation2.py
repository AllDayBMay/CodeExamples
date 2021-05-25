"""
Below is the code for one of the questions for my Scientific Computing Final at Arizona State University.
I share it here because I wanted a shareable demonstration of my experiences with python, numpy, and pyplot.
The purpose of this code was first to plot a function that had been determined algebraically in a prior question,
and to plot it against a matrix of values that had been solved using the same formula.
"""

from math import *
from numpy import zeros

#Define function to be plotted
u = lambda x,a: (1+(exp(2*a)-1)*x-exp(2*a*x))/(2*a*(exp(2*a)-1))

from matplotlib.pyplot import close, figure, plot, axis, grid, xlabel, ylabel, legend, savefig, subplot, show

#This function gets the input data from a previously solved matrix to be plotted.
def adjustdata(myinputvals, myinputexp):
    myarray = []
    myvals = []
    myexp = []
    myoutput = []
    with open(myinputvals) as myinput:
        for line in myinput:
            myarray.append(line)
    myarray[0]=0.
    myarraylength = len(myarray)
    for i in range(myarraylength):
        myvals.append(float(myarray[i]))
        i+=1
    myarray = []
    with open(myinputexp) as myinput:
        for line in myinput:
            myarray.append(line)
    myarray[0]=0.
    myarraylength = len(myarray)
    for i in range(myarraylength):
        myexp.append(float(myarray[i]))
        i+=1
    for i in range(myarraylength):
        thisexp = myexp[i]
        myoutput.append(myvals[i]*(10.**(thisexp)))
        i+=1
    return myoutput

#Close all previous graphs, and then open a new one with the first data.
close()
figure(1)
xspan=[0.,1.]
a=1.
colors = 'kbg'
#Getting the input matrices for the relevant x-values and their corresponding exponents
data1 = 'p2saval.txt'
data2 = 'p2saexp.txt'
fa=adjustdata(data1,data2)
z = 0
N=len(fa)
#Create zero-matrices with the correct dimensions.
x = zeros(N)
y = zeros(N)
ae = zeros(N)
#Populate the matrices with the input data, and apply the equation to it.
for z in range(0,N):
    x[z]=z/N
    y[z] = u(x[z],a)
    ae[z] = abs((fa[z]-y[z])/y[z])*100.
#Plotting the direct equation
plot(x,y,label='Direct Equation', linewidth=2, color='b')
#Plotting the input matrices
plot(x,fa,label= "p2_sgtsv", linewidth=2, color='r')
axis(xspan+[0.,0.2])
grid('on')
xlabel(r'$x$', fontsize = 16)
ylabel(r'$u(x)$', fontsize = 16)
legend(loc='upper right')
savefig('up2sa.eps')

#Below, the process is repeated in different graphs for
#different matrix sizes and exponents in the original equation.
figure(2)
a=10.
data1 = 'p2sbval.txt'
data2 = 'p2sbexp.txt'
fb=adjustdata(data1,data2)
z=0
N=len(fb)
x2 = zeros(N)
y2 = zeros(N)
ae2 = zeros(N)
for z in range(0,N):
    x2[z]=z/N
    y2[z] = u(x2[z],a)
    ae2[z] = abs((fb[z]-y2[z])/y2[z])*100.
plot(x2,y2,label='Direct Equation',linewidth=2, color='b')
plot(x2,fb,label='p2_sgtsv', linewidth=2, color='r')
axis(xspan+[0.,0.2])
grid('on')
xlabel(r'$x$', fontsize = 16)
ylabel(r'$u(x)$', fontsize = 16)
legend(loc='upper right')
savefig('up2sb.eps')

figure(3)
data1 = 'p2scval.txt'
data2 = 'p2scexp.txt'
fc=adjustdata(data1,data2)
z=0
N=len(fc)
x3 = zeros(N)
y3 = zeros(N)
ae3 = zeros(N)
for z in range(0,N):
    x3[z]=z/N
    y3[z] = u(x3[z],a)
    ae3[z] = abs((fc[z]-y3[z])/y3[z])*100.
plot(x3,y3,label='Direct Equation',linewidth=2, color='b')
plot(x3,fc,label='p2_sgtsv',linewidth=2, color='r')
axis(xspan+[0.,0.2])
grid('on')
xlabel(r'$x$', fontsize=16)
ylabel(r'$u(x)$',fontsize=16)
legend(loc='upper right')
savefig('up2sc.eps')

figure(4)
data1 = 'p2sdval.txt'
data2 = 'p2sdexp.txt'
fd=adjustdata(data1,data2)
z=0
N=len(fd)
x4 = zeros(N)
y4 = zeros(N)
ae4 = zeros(N)
for z in range(0,N):
    x4[z]=z/N
    y4[z] = u(x4[z],a)
    ae4[z] = abs((fd[z]-y4[z])/y4[z])*100.
plot(x4,y4,label='Direct Equation',linewidth=2, color='b')
plot(x4,fd,label='p2_sgtsv',linewidth=2, color='r')
axis(xspan+[0.,0.2])
grid('on')
xlabel(r'$x$', fontsize=16)
ylabel(r'$u(x)$',fontsize=16)
legend(loc='upper right')
savefig('up2sd.eps')


figure(5)
data1 = 'p2daval.txt'
data2 = 'p2daexp.txt'
ga=adjustdata(data1,data2)
z=0
a=1.
N=len(ga)
x5 = zeros(N)
y5 = zeros(N)
ae5 = zeros(N)
for z in range(0,N):
    x5[z]=z/N
    y5[z] = u(x5[z],a)
    ae5[z] = abs((ga[z]-y5[z])/y5[z])*100.
plot(x5,y5,label='Direct Equation',linewidth=2, color='b')
plot(x5,ga,label='p2_dgtsv',linewidth=2, color='r')
axis(xspan+[0.,0.2])
grid('on')
xlabel(r'$x$', fontsize=16)
ylabel(r'$u(x)$',fontsize=16)
legend(loc='upper right')
savefig('up2da.eps')

figure(6)
data1 = 'p2dbval.txt'
data2 = 'p2dbexp.txt'
gb=adjustdata(data1,data2)
z=0
a=10.
N=len(gb)
x6 = zeros(N)
y6 = zeros(N)
ae6 = zeros(N)
for z in range(0,N):
    x6[z]=z/N
    y6[z] = u(x6[z],a)
    ae6[z] = abs((gb[z]-y6[z])/y6[z])*100.
plot(x6,y6,label='Direct Equation', linewidth=2, color='b')
plot(x6,gb,label='p2_dgtsv', linewidth=2, color='r')
axis(xspan+[0.,0.2])
grid('on')
xlabel(r'$x$', fontsize=16)
ylabel(r'$u(x)$',fontsize=16)
legend(loc='upper right')
savefig('up2db.eps')

figure(7)
data1 = 'p2dcval.txt'
data2 = 'p2dcexp.txt'
gc=adjustdata(data1,data2)
z=0
N=len(gc)
x7 = zeros(N)
y7 = zeros(N)
ae7 = zeros(N)
for z in range(0,N):
    x7[z]=z/N
    y7[z] = u(x7[z],a)
    ae7[z] = abs((gc[z]-y7[z])/y7[z])*100.
plot(x7,y7,label='Direct Equation',linewidth=2, color='b')
plot(x7,gc,label='p2_dgtsv',linewidth=2, color='r')
axis(xspan+[0.,0.2])
grid('on')
xlabel(r'$x$', fontsize=16)
ylabel(r'$u(x)$',fontsize=16)
legend(loc='upper right')
savefig('up2dc.eps')

figure(8)
data1 = 'p2ddval.txt'
data2 = 'p2dd2exp.txt'
gd=adjustdata(data1,data2)
z=0
N=len(gd)
x8 = zeros(N)
y8 = zeros(N)
ae8 = zeros(N)
for z in range(0,N):
    x8[z]=z/N
    y8[z] = u(x8[z],a)
    ae8[z] = abs((gd[z]-y8[z])/y8[z])*100.
plot(x8,y8,label='Direct Equation',linewidth=2, color='b')
plot(x8,gd,label='p2_dgtsv',linewidth=2, color='r')
axis(xspan+[0.,0.2])
grid('on')
xlabel(r'$x$', fontsize=16)
ylabel(r'$u(x)$',fontsize=16)
legend(loc='upper right')
savefig('up2dd.eps')


#Below, the absolute error between the matrix values
#and the calculated values are graphed.
figure(9)
plot(x,ae,label='Absolute Error', linewidth=2, color='g')
axis(xspan+[0.,1000.])
grid('on')
xlabel(r'$x$',fontsize=16)
ylabel(r'$ae$',fontsize=16)
legend(loc='upper right')
savefig('ae1.eps')

figure(10)
plot(x2,ae2,label='Absolute Error', linewidth=2, color='g')
axis(xspan+[0.,1000.])
grid('on')
xlabel(r'$x$',fontsize=16)
ylabel(r'$ae$',fontsize=16)
legend(loc='upper right')
savefig('ae2.eps')

figure(11)
plot(x3,ae3,label='Absolute Error', linewidth=2, color='g')
axis(xspan+[0.,1000.])
grid('on')
xlabel(r'$x$',fontsize=16)
ylabel(r'$ae$',fontsize=16)
legend(loc='upper right')
savefig('ae3.eps')

figure(12)
plot(x4,ae4,label='Absolute Error', linewidth=2, color='g')
axis(xspan+[0.,1000.])
grid('on')
xlabel(r'$x$',fontsize=16)
ylabel(r'$ae$',fontsize=16)
legend(loc='upper right')
savefig('ae4.eps')

figure(13)
plot(x5,ae5,label='Absolute Error', linewidth=2, color='g')
axis(xspan+[0.,1000.])
grid('on')
xlabel(r'$x$',fontsize=16)
ylabel(r'$ae$',fontsize=16)
legend(loc='upper right')
savefig('ae5.eps')

figure(14)
plot(x6,ae6,label='Absolute Error', linewidth=2, color='g')
axis(xspan+[0.,1000.])
grid('on')
xlabel(r'$x$',fontsize=16)
ylabel(r'$ae$',fontsize=16)
legend(loc='upper right')
savefig('ae6.eps')

figure(15)
plot(x7,ae7,label='Absolute Error', linewidth=2, color='g')
axis(xspan+[0.,1000.])
grid('on')
xlabel(r'$x$',fontsize=16)
ylabel(r'$ae$',fontsize=16)
legend(loc='upper right')
savefig('ae7.eps')

figure(16)
plot(x8,ae8,label='Absolute Error', linewidth=2, color='g')
axis(xspan+[0.,1000.])
grid('on')
xlabel(r'$x$',fontsize=16)
ylabel(r'$ae$',fontsize=16)
legend(loc='upper right')
savefig('ae8.eps')

show()