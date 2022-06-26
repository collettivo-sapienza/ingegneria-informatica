import itertools
import math
import scipy.special

#prob seconda rossa se almeno una rossa
#= prob tutte e tre rosse e seconda rossa
#+ prob 2 rosse e seconda rossa
#+prob 1 rossa e seconda rossa
#=
#(1/4)^3
#+(1/4)^2 * 2/3
#+(1/4) * 1/3
#a = (26/52)*(25/51)*(24/50) + (26/52)*(25/51)*(26/50)*(2/3) + (26/52)*(26/51)*(25/50)*(1/3)
a = (26/52)*(25/51)*(26/50)*(2/3) + (26/52)*(26/51)*(25/50)*(1/3)
#   R|RRR +               vabbeporcodio sticazzi piccioni scemo      R|RRB                       + R|RBB
print (a)
b = 13/45
print(b)
