#!/usr/bin/env python3
################
#egtsimplex
#Copyright © 2016 Marvin A. Böttcher
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
#################
import matplotlib.pyplot as plt
import numpy as np
import egtsimplex

#define function of x=[x0,x1,x2] and t to plot dynamics on simplex
def f(x,t):
    A=np.array([[0,1,-1],[-1,0,1],[1,-1,0]])
    phi=(x.dot(A.dot(x)))
    x0dot=x[0]*(A.dot(x)[0]-phi)
    x1dot=x[1]*(A.dot(x)[1]-phi)
    x2dot=x[2]*(A.dot(x)[2]-phi)
    return [x0dot,x1dot,x2dot]


#initialize simplex_dynamics object with function
dynamics=egtsimplex.simplex_dynamics(f)

#plot the simplex dynamics
fig,ax=plt.subplots()
dynamics.plot_simplex(ax)
plt.show()
