from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the clipping window coordinates
x_min, y_min = 50, 50
x_max, y_max = 250, 250

# Function to determine the region code of a point
def compute_code(x, y):
    code = 0
    if x < x_min:
        code |= 1  # Set bit 1 (binary: 001)
    elif x > x_max:
        code |= 2  # Set bit 2 (binary: 010)
    if y < y_min:
        code |= 4  # Set bit 3 (binary: 100)
    elif y > y_max:
        code |= 8  # Set bit 4 (binary: 1000)
    return code

# Function to clip a line segment using Cohen-Sutherland algorithm
def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    
    accept = False
    while True:
        if not (code1 | code2):  # Both endpoints are inside the window
            accept = True
            break
        elif code1 & code2:  # Both endpoints are outside the same region
            break
        else:
            x, y = 0, 0
            code_out = code1 if code1 else code2
            
            if code_out & 1:  # Point is to the left of the clipping window
                x = x_min
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            elif code_out & 2:  # Point is to the right of the clipping window
                x = x_max
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            elif code_out & 4:  # Point is below the clipping window
                y = y_min
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
            elif code_out & 8:  # Point is above the clipping window
                y = y_max
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
            
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)
    
    if accept:
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    
    # Define the line segment
    x1, y1 = 20, 120
    x2, y2 = 200, 300
    
    # Draw the original line segment
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    
    # Clip and draw the line segment using Cohen-Sutherland algorithm
    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    cohen_sutherland(x1, y1, x2, y2)

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
glutInitWindowSize(400, 400)
glutCreateWindow(b"Cohen-Sutherland Line Clipping")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
