import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants for orbit and animation
earth_radius = 5  # Arbitrary radius for visual representation
moon_radius = 2
orbit_radius = 10
frames = 100
period = 28  # Period of the Moon's orbit in days

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-orbit_radius - earth_radius, orbit_radius + earth_radius)
ax.set_ylim(-orbit_radius - earth_radius, orbit_radius + earth_radius)

# Create Earth and Moon objects
earth = plt.Circle((0, 0), radius=earth_radius, color='blue')
moon = plt.Circle((orbit_radius, 0), radius=moon_radius, color='gray')

# Function to update the satellite's position
def animate(frame):
    angle = 2 * np.pi * frame / frames * period  # Calculate angle for smooth animation
    satellite_x = orbit_radius * np.cos(angle)
    satellite_y = orbit_radius * np.sin(angle)
    satellite.center = (satellite_x, satellite_y)
    return satellite,

# Add satellite to plot
satellite = plt.Circle((orbit_radius, 0), radius=0.5, color='red')
ax.add_patch(earth)
ax.add_patch(moon)
ax.add_patch(satellite)

# Create animation
ani = animation.FuncAnimation(
    fig, animate, interval=50, frames=frames, blit=True, repeat=True
)

plt.title("Satellite Animation")
plt.show()
