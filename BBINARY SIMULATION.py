import pygame
import math
import matplotlib.pyplot as plt

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1380, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary Star Simulation")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
## Consider 1 Solar mass to be 25
## consider 0.01AU as 100 pixels
# Star parameters
STAR1_RADIUS = 20
STAR2_RADIUS = 20
STAR1_MASS = float(input('Enter the mass of the first star: ')) #59.725
STAR2_MASS = float(input('Enter the mass of the second star: '))#58.175
INITIAL_DISTANCE_1 = float(input('Enter the distance between the center of mass and star1: '))#406
INITIAL_DISTANCE_2 = float(input('Enter the distance between the center of mass and star2: '))#417
G = 1.0  # Grav constant

# Total Mass
TOTAL_MASS = STAR1_MASS + STAR2_MASS

# initial position of stars.
star1_x = WIDTH // 2 - INITIAL_DISTANCE_1 * STAR2_MASS / TOTAL_MASS
star1_y = HEIGHT // 2
star1_vx = 0.0
star1_vy = math.sqrt(G * STAR2_MASS / INITIAL_DISTANCE_1) * STAR1_MASS / TOTAL_MASS

star2_x = WIDTH // 2 + INITIAL_DISTANCE_2 * STAR1_MASS / TOTAL_MASS
star2_y = HEIGHT // 2
star2_vx = 0.0
star2_vy = -math.sqrt(G * STAR1_MASS / INITIAL_DISTANCE_2) * STAR2_MASS / TOTAL_MASS

# Center of mass position
com_x = (STAR1_MASS * star1_x + STAR2_MASS * star2_x) / TOTAL_MASS
com_y = (STAR1_MASS * star1_y + STAR2_MASS * star2_y) / TOTAL_MASS

# Lists to store positions for plotting
star1_positions_x = []
star1_positions_y = []
star2_positions_x = []
star2_positions_y = []
star1_velocity_x = []
star1_velocity_y = []
star2_velocity_x = []
star2_velocity_y = []
distance_list=[]
time_list=[]


# SIMULATION LOOP
time=0
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate the distance vector and its magnitude
    dx = star2_x - star1_x
    dy = star2_y - star1_y
    distance = math.sqrt(dx**2 + dy**2)

    # Calculate the gravitational force
    force = G * STAR1_MASS * STAR2_MASS / (distance**2)

    # Calculate the acceleration components for each star
    ax1 = force * dx / (STAR1_MASS * distance)
    ay1 = force * dy / (STAR1_MASS * distance)
    ax2 = -force * dx / (STAR2_MASS * distance)
    ay2 = -force * dy / (STAR2_MASS * distance)

    # Update the velocities and positions of the stars
    star1_vx += ax1
    star1_vy += ay1
    star1_x += star1_vx
    star1_y += star1_vy

    star2_vx += ax2
    star2_vy += ay2
    star2_x += star2_vx
    star2_y += star2_vy

    # Update the center of mass position
    com_x = (STAR1_MASS * star1_x + STAR2_MASS * star2_x) / TOTAL_MASS
    com_y = (STAR1_MASS * star1_y + STAR2_MASS * star2_y) / TOTAL_MASS

    # Store positions for plotting
    star1_positions_x.append(star1_x - com_x + WIDTH // 2)
    star1_positions_y.append(star1_y - com_y + HEIGHT // 2)
    star2_positions_x.append(star2_x - com_x + WIDTH // 2)
    star2_positions_y.append(star2_y - com_y + HEIGHT // 2)

    star1_velocity_x.append(star1_vx)
    star1_velocity_y.append(star1_vy)
    star2_velocity_x.append(star2_vx)
    star2_velocity_y.append(star2_vy)
    distance_list.append(distance)
    time_list.append(time)
    time+=1

    # Draw the stars relative to the center of mass
    pygame.draw.circle(screen, 'ORANGE', (int(star1_x - com_x + WIDTH // 2), int(star1_y - com_y + HEIGHT // 2)), STAR1_RADIUS)
    pygame.draw.circle(screen, 'YELLOW', (int(star2_x - com_x + WIDTH // 2), int(star2_y - com_y + HEIGHT // 2)), STAR2_RADIUS)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

# Plot the positions of star 1 and star 2
plt.figure(figsize=(8, 6))
plt.plot(star1_positions_x, star1_positions_y, label='Star 1', color='ORANGE')
plt.plot(star2_positions_x, star2_positions_y, label='Star 2', color='YELLOW')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Positions of Star 1 and Star 2')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(time_list, distance_list, label='distance', color='black')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.title('Distance Vs Time of Star 1 and Star 2')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()