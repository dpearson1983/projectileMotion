import math # for sin, cos, and pi
import sys # To process command line arguments

v_0 = -math.pi; theta = -math.pi; dt = -math.pi; m = -math.pi; C = -math.pi
for i in range(1,len(sys.argv)):
    if (sys.argv[i] == "-v0"):
        v_0 = float(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-theta"):
        theta = float(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-dt"):
        dt = float(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-m"):
        m = float(sys.argv[i + 1])
        i += 1
    elif (sys.argv[i] == "-C"):
        C = float(sys.argv[i + 1])
        i += 1

g = 9.8 # Earth's surface gravity in units of m/s^2

# Compute the acceleration assuming gravity and drag force
def acceleration(v_x, v_y, C, m):
    a_x = -C*v_x*math.sqrt(v_x*v_x + v_y*v_y)/m
    a_y = -g - C*v_y*math.sqrt(v_x*v_x + v_y*v_y)/m
    return a_x, a_y

# Update the position and velocity of the projectile
def update(x, y, v_x, v_y, a_x, a_y, dt):
    x = x + v_x*dt + 0.5*a_x*dt*dt
    y = y + v_y*dt + 0.5*a_y*dt*dt
    v_x = v_x + a_x*dt
    v_y = v_y + a_y*dt
    return x, y, v_x, v_y

# Get the initial input
if (len(sys.argv) < 6):
    if (v_0 == -math.pi):
        v_0 = float(input("What is the magnitude of the initial velocity?: "))
    if (theta == -math.pi):
        theta = float(input("What is the launch angle in degrees?: "))
    if (dt == -math.pi):
        dt = float(input("What is the size of the time step?: "))
    if (m == -math.pi):
        m = float(input("What is the projectile mass?: ")) # golf ball ~ 0.04593 kg
    if (C == -math.pi):
        C = float(input("What is the drag coefficient?: ")) # golf ball ~ 4E-4 kg/m

# Break the initial velocity into components
v_x = v_0*math.cos(theta*math.pi/180.0)
v_y = v_0*math.sin(theta*math.pi/180.0)

# Open file for output
outFile = open("projectileDragData.txt","w")

# Set some initial values
t = 0
x = 0
y = 0
y_max = 0
inFlight = True

# Run the loop for the desired number of time steps, output to file at each step
while (inFlight):
    a_x, a_y = acceleration(v_x, v_y, C, m)
    x, y, v_x, v_y = update(x, y, v_x, v_y, a_x, a_y, dt)
    t += dt
    if (y >= 0):
        outFile.write(str(t) + " " + str(x) + " " + str(y) + " " + str(v_x) + 
                      " " + str(v_y) + " " + str(a_x) + " " + str(a_y) + "\n")
        if (y > y_max):
            y_max = y
    else:
        inFlight = False

# Close the file
outFile.close()

# Print some summary statistics
print("The maximum height was", y_max)
print("The horizontal range was", x)