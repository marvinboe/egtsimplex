# egtsimplex
Plotting a simplex for three player evolutionary games with python.

Takes an arbitrary 3d function of 3 parameters of the form
$dx/dt=f(x)$ with the frequencies of the three types adding up to
one, that is $x_0+x_1+x_2=1$. From this a simplex plot with arrows 
pointing into the direction of the dynamics and color codes 
denoting the strength of change is created.

basic usage:
`import egtsimplex
#define function for the dynamics
def f(x):
    return [x[0],-x[1],x[2]]

#initialize simplex_dynamics object with function
dynamics=egtsimplex.simplex_dynamics(f)

#plot the simplex dynamics
dynamics.plot()`



