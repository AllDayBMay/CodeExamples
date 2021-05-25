%Below is the code for one of the questions for my Scientific Computing Final at Arizona State University
%I share it here because I wanted a shareable demonstration of my experiences with Matlab.
%While this particular code does not involve any matrix manipulation,
%that was primarily what I used Matlab for.
%Unfortunately, I do not have any examples of this to share that would not involve sharing
%questions that my professors assigned and may not wish to have made public.


%First, we define all the variables
a, b, c, m, q, p, mu, lam = 2;
x = [0:1000000];
x = x/1000;
%Then, we define the given equations to be graphed
eqn1 = a*log(x)+b;
eqn2 = m*x+c;
eqn3 = q*x.^p;
eqn4 = mu*exp(lam*x);

%The first four plots are for equation 1
figure(1)
plot(x,eqn1)
title('Linear-Linear, Equation 1', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([-1 11])
ylim([-10 10])
figure(2)
semilogy(x,eqn1)
title('Linear-Log, Equation 1', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([0 11])
ylim([0.001 10])
figure(3)
semilogx(x,eqn1)
title('Log-Linear, Equation 1', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([0.001 100])
ylim([-13 10])
figure(4)
loglog(x,eqn1)
title('Log-Log, Equation 1', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([-10 10])
ylim([0.01 10])

%The next four plots are for equation 2
figure(5)
plot(x,eqn2)
title('Linear-Linear, Equation 2', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([-1 11])
ylim([-1 25])
figure(6)
semilogy(x,eqn2)
title('Linear-Log, Equation 2', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([1 20])
ylim([5 60])
figure(7)
semilogx(x,eqn2)
title('Log-Linear, Equation 2', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([0.001 60])
ylim([-1 31])
figure(8)
loglog(x,eqn2)
title('Log-Log,Equation 2', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([0 1000])
ylim([0 1000])

%The next four are for equation 3
figure(9)
plot(x,eqn3)
title('Linear-Linear, Equation 3', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([-1 15])
ylim([-1 500])
figure(10)
semilogy(x,eqn3)
title('Linear-Log, Equation 3', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([-1 11])
ylim([0 10^3])
figure(11)
semilogx(x,eqn3)
title('Log-Linear, Equation 3', 'Fontsize', 10)
ylabel('y')
xlabel('x')
grid onxlim([-1 60])
ylim([-1 1000])
figure(12)
loglog(x,eqn3)
title('Log-Log, Equation 3', 'Fontsize', 10)
ylabel('y')
xlabel('x')
grid onxlim([-1 60])
ylim([-1 1000])
figure(12)
loglog(x,eqn3)
title('Log-Log, Equation 3', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid onxlim([0 10])
ylim([0 1000])

%The last four are for equation 4
figure(13)
plot(x,eqn4)
title('Linear-Linear, Equation 4', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid onxlim([0 3.5])
ylim([-1 1000])
figure(15)
semilogx(x,eqn4)
title('Log-Linear, Equation 4', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid on
xlim([-1 10.2])
ylim([-1 600])
figure(16)
loglog(x,eqn4)
title('Log-Log, Equation 4', 'Fontsize',10)
ylabel('y')
xlabel('x')
grid onxlim([-1 10.2])
ylim([0 500])

