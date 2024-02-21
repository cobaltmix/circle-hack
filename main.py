import pyautogui
import math
import time
import pygame

pygame.init()


def draw_circle(radius, center_x, center_y, steps=10000):
    # Suppresses the default pause of pyautogui to make movements instant
    pyautogui.PAUSE = 0.0000001

    # Calculate points around the circle's perimeter
    points = []
    for i in range(steps):
        angle = math.radians(float(i) / steps * 360.0)
        x = center_x + (radius * math.cos(angle))
        y = center_y + (radius * math.sin(angle))
        points.append((x, y))

    # Move to the starting position and press down the left mouse button
    pyautogui.moveTo(points[0])
    pyautogui.mouseDown()

    # Draw the circle by hitting each point extresmely quickly
    for point in points:
        pyautogui.moveTo(point)

    # Complete the circle by moving to the starting position
    pyautogui.moveTo(points[0])

    # Release the left mouse button
    pyautogui.mouseUp()


# Get the size of the primary monitor.
screen_width, screen_height = pyautogui.size()

print(screen_width, screen_height)

# Calculate the center of the screen.
center_x = 768*(1080/850)-15
center_y = 444*(1080/850)-8


# Set the radius for the circle.
circle_radius = 250  # Adjust the radius as needed.

time.sleep(2)  # Wait for 5 seconds before starting.x

# Draw the circle fast.
draw_circle(circle_radius, center_x, center_y)
