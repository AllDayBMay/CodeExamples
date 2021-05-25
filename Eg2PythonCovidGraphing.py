"""
Below is the code for one of the questions for my Scientific Computing Final at Arizona State University.
I share it here because I wanted a shareable demonstration of my experiences with python, numpy, and pyplot.
The purpose of this code was to plot the rates of Covid-19 infections and susceptibility over time, 
and in relation to one another.
"""

import math
from numpy import *
from numpy import zeros
from numpy import pi 
from scipy.integrate import ode
from matplotlib.pyplot import close, figure, plot, axis, grid, xlabel, ylabel, subplot, legend, savefig, show
    
#Define function for predicted infection over time.
def f(t,y,params):
    s,i = y # retrieve s and i from 2x1 vector y
    mu,gamma,alpha,w,b0 = params # retrieve parameters from params list
    dsdt = mu*(1.0-s)-(b0*alpha*sin(w*t)+b0)*s*i #incorporating beta as determined by part a of Question 3
    didt = (b0*alpha*sin(w*t)+b0)*s*i-(mu+gamma)*i #incorporating beta as determined by part a of Question 3
    return array([dsdt,didt])

#Heun/Euler's method for plotting predictions of infections and susceptibility rates over time
def myHeun(f,tspan,y0,N,params):
    h = float(tspan[1]-tspan[0])/N # time step, as defined by problem
    t = tspan[0]; y = y0
    tout = zeros((N+1,1)); yout = zeros((N+1,2)) # reserve space for output
    tout[0] = t; yout[0] = y # set initial t and y
    for n in range(1,N+1): # n=1..N
        f1 = f(t,y,params) # y' @ current t
        f2 = f(t+h,y+h*f1,params) #f2 for Heun's method (Improved Euler)
        t += h # update t
        y += h*f1 # update y
        tout[n] = t; yout[n] = y
    return tout,yout

#Method for plotting infections as a function of susceptibility
def odesolve(f,tspan,y0,N,params):
    r = ode(f)
    r.set_integrator('vode',rtol=1e-6)
    h = float(tspan[1]-tspan[0])/N # time step, as defined by problem
    tout = zeros((N+1,1)); yout = zeros((N+1,2)) # initialize output
    n = 0
    r.set_initial_value(y=y0,t=tspan[0]) # initial condition
    r.set_f_params(params) # parameters
    tout[0,:] = r.t; yout[0,:] = r.y;
    while r.successful() and n < N:
        r.integrate(r.t+h) # integrate ODE r from t to t+h
        n += 1; tout[n,:] = r.t; yout[n,:] = r.y; # record new values
    return tout,yout

#Get initial ranges, data, and use functions to solve.
tspan = [0.,1000.] # initial and final times
y0 = s0,i0 = [.1,.1] # initial values
t=0
params = mu,gamma,alpha,w,b0 = [0.05,0.3,0.7,0.2*pi,0.8] # parameters
N=10000 # "exact" solution plotted using sufficiently many points
t,y = odesolve(f,tspan,y0,N,params)
t = t[:,0]; s = y[:,0]; i = y[:,1]; # extract variables
N = 10000 # Improved Euler solution with step size (tspan[1]-tspan[0])/N=10000
t1,y1 = myHeun(f,tspan,y0,N,params)
t1 = t1[:,0]; s1 = y1[:,0]; i1 = y1[:,1]; # extract variables

#Plot results
close() # if figure already open
figure(1) # open figure
subplot(2,1,1) # partitions figure as 2x1 and select first (top)
plot(t,s,'b-',t1,s1,'bo',t,i,'r-',t1,i1,'ro',linewidth=2,markersize=5)
legend([r'$s(t)$','Euler',r'$i(t)$','Euler'])
axis(tspan+[0.,1.]) # [0.,100.,0.,1.]
grid('on')
subplot(2,1,2) # partitions figure as 2x1 and select second (bottom)
plot(s,i,'k-',s1,i1,'ro',linewidth=2,markersize=5)
legend(['exact','Euler'],loc='best')
xlabel(r'$s$')
ylabel(r'$i$')
axis([0.,.7,0.,.2])
grid('on')
savefig('MAT420FinalQ3C.eps') # export figure as eps
