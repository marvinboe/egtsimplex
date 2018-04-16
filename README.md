# egtsimplex
Plotting a simplex for three player evolutionary games with python.
<img src"images/example_plot.png" width="500" height="400" />

!Needs python 3.5 or higher!

Takes an arbitrary 3d function of 3 parameters of the form
$dx/dt=f(x,t)$ with the frequencies of the three types adding up to
one, that is $x_0+x_1+x_2=1$. From this a simplex plot with arrows 
pointing into the direction of the dynamics and color codes 
denoting the strength of change is created. As a bonus, the fixed
points of the dynamics are also shown (without stability, though).

basic usage:

1. initialize egtsimplex-object with function f(x,t)
2. use the plot_simplex() method to plot the simplex

*see file "./plot_example.py" for an example*



