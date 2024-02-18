from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Triangle vertices
triangle_vertices = [(100, 100), (200, 100), (150, 200)]

# Rotation center
rotation_center = (150, 150)

# Rotation angle (in degrees)
rotation_angle = 30  # Change this angle as needed

# Function to rotate a point around another point
def rotate_point(point, center, angle):
    angle_rad = math.radians(angle)  # Convert angle to radians
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)

    translated_x = point[0] - center[0]
    translated_y = point[1] - center[1]

    rotated_x = translated_x * cos_theta - translated_y * sin_theta + center[0]
    rotated_y = translated_x * sin_theta + translated_y * cos_theta + center[1]

    return rotated_x, rotated_y

# Function to draw the original and rotated triangles side by side
def draw_triangles():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white

    # Draw the original triangle
    glBegin(GL_TRIANGLES)
    for vertex in triangle_vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

    # Draw the rotated triangle
    glBegin(GL_TRIANGLES)
    for vertex in triangle_vertices:
        rotated_vertex = rotate_point(vertex, rotation_center, rotation_angle)
        glVertex2f(rotated_vertex[0] + 200, rotated_vertex[1])  # Shift the rotated triangle to the right
    glEnd()

    glFlush()

# Function to handle window resizing
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 400)
glutCreateWindow(b"Original and Rotated Triangles in 2D Space")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(draw_triangles)
glutReshapeFunc(reshape)
glutMainLoop()
