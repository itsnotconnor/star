## Star Tracker Frame to Spacecraft Frame


import math
import numpy as np

#float
x_star_float = 0.0#coordiantes
y_star_float = 0.0
z_star_float = 0.0


ra_star_float =  0.0#degrees
dec_star_float = 0.0#degrees


def calcXyzFromRaDec( ra, dec ):
    x_star = np.cos(dec)*np.cos(ra) 
    y_star = np.cos(dec)*np.sin(ra)
    z_star = sin(dec)
    return [x_star, y_star, z_star]


## ECI frame

#Direction cosine matrix
# [A]

#unit vectors 
u_u_vector = [1,1,1]
v_u_vector = [1,1,1]
w_u_vector = [1,1,1]

DCM = np.matrix( [ u_u_vector, v_u_vector, w_u_vector ] )


print(DCM) 


