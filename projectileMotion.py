import math # for sin, cos, and pi

g = 9.8 # Earth's surface gravity in units of m/s^2

# Get the initial input
v_0 = float(input("What is the magnitude of the initial velocity?: "))
theta = float(input("What is the launch angle in degrees?: "))
N_steps = int(input("How many time-steps?: "))

# Break the initial velocity into components
v_x0 = v_0*math.cos(theta*math.pi/180.0)
v_y0 = v_0*math.sin(theta*math.pi/180.0)

# Compute time of flight and size of time step
t_flight = 2.0*v_y0/g
delta_t = t_flight/float(N_steps)

# Open file for output
outFile = open("projectileData.txt","w")

# Set some initial values
x = 0
y = 0
v_y = v_y0
y_max = 0

# Run the loop for the desired number of time steps, output to file at each step
for i in range(1,N_steps + 1):
    x = x + v_x0*(delta_t)
    y = y + v_y*(delta_t) - 0.5*g*(delta_t)*(delta_t)
    v_y = v_y - g*(delta_t)
    outFile.write(str(i*delta_t) + " " + str(x) + " " + str(y) + " " + str(v_x0) 
                  + " " + str(v_y) + "\n")
    if (y > y_max):
        y_max = y

# Close the file
outFile.close()

# Print some summary statistics
print("The maximum height was", y_max)
print("The horizontal range was", x)