# egtsimplex
Plotting a simplex for three player evolutionary games with python.

!Needs python 3.5 or higher!

Takes an arbitrary 3d function of 3 parameters of the form
$dx/dt=f(x)$ with the frequencies of the three types adding up to
one, that is $x_0+x_1+x_2=1$. From this a simplex plot with arrows 
pointing into the direction of the dynamics and color codes 
denoting the strength of change is created.

basic usage:
1. initialize egtsimplex-object with function f(x,t)
2. use the plot_simplex() method to plot the simplex
see file "./plot_example.py" for an example



