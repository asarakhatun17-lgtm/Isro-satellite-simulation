import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 1. SETTING UP THE REAL-WORLD PHYSICS ---
G = 6.67430e-11     # Gravitational constant 
M_earth = 5.972e24  # Mass of Earth
R_earth = 6371000   # Radius of Earth

# 1. LEO Satellite (Red - Closest & Fastest)
r_leo = R_earth + 400000
w_leo = np.sqrt(G * M_earth / r_leo) / r_leo

# 2. GEO Satellite (Green - Mid distance & Mid speed)
r_geo = R_earth + 35786000
w_geo = np.sqrt(G * M_earth / r_geo) / r_geo

# 3. The Moon (White - Farthest & Slowest)
r_moon = 384400000 # Distance to Moon in meters (~384,400 km)
w_moon = np.sqrt(G * M_earth / r_moon) / r_moon

# Time array: Simulating 2 days of real time (172800 seconds)
# Frame rate badha diya hai taaki smooth chale
t = np.linspace(0, 172800, 500) 

# Coordinates calculate karna
x_leo = r_leo * np.cos(w_leo * t)
y_leo = r_leo * np.sin(w_leo * t)

x_geo = r_geo * np.cos(w_geo * t)
y_geo = r_geo * np.sin(w_geo * t)

x_moon = r_moon * np.cos(w_moon * t)
y_moon = r_moon * np.sin(w_moon * t)

# --- 2. DRAWING SPACE ---
fig, ax = plt.subplots(figsize=(9, 9))
fig.patch.set_facecolor('black') 
ax.set_facecolor('black')        
ax.set_aspect('equal')

# Drawing the Earth (Thoda bada dikhaya hai visibility ke liye)
earth_circle = plt.Circle((0, 0), R_earth * 3, color='#0f52ba', label="Earth")
ax.add_patch(earth_circle)

# Drawing Orbit Paths 
theta = np.linspace(0, 2*np.pi, 100)
ax.plot(r_leo * np.cos(theta), r_leo * np.sin(theta), 'w--', linewidth=0.3, alpha=0.5)
ax.plot(r_geo * np.cos(theta), r_geo * np.sin(theta), 'w--', linewidth=0.5, alpha=0.5)
ax.plot(r_moon * np.cos(theta), r_moon * np.sin(theta), 'w--', linewidth=0.8, alpha=0.3)

# Setting up the Objects
sat_leo, = ax.plot([], [], 'ro', markersize=4, label="LEO Satellite (Fastest)")
sat_geo, = ax.plot([], [], 'go', markersize=6, label="GEO Satellite")
moon_obj, = ax.plot([], [], 'wo', markersize=10, label="Moon (Slowest)")

# Scaling the screen so the HUGE Moon orbit fits
limit = r_moon * 1.1
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)
ax.set_title("Orbital Physics: LEO, GEO & The Moon", color='white', fontsize=16, fontweight='bold')
ax.legend(loc="upper right", facecolor='black', labelcolor='white', fontsize=9)

# --- 3. THE ANIMATION LOGIC ---
def update(frame):
    sat_leo.set_data([x_leo[frame]], [y_leo[frame]])
    sat_geo.set_data([x_geo[frame]], [y_geo[frame]])
    moon_obj.set_data([x_moon[frame]], [y_moon[frame]])
    return sat_leo, sat_geo, moon_obj

# Animating the plot
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)
plt.show()
