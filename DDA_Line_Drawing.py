from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to draw a point
def drawPoint(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Function to draw a line using DDA algorithm
def drawLineDDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate increment in x and y for each step
    incX = dx / steps
    incY = dy / steps

    # Put pixel for each step
    x = x1
    y = y1
    for i in range(steps):
        drawPoint(round(x), round(y))
        x += incX
        y += incY

# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white

    # Coordinates of two points
    x1, y1 = 10, 12
    x2, y2 = 30, 35

    drawLineDDA(x1*10, y1*10, x2*10, y2*10)

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
glutInitWindowSize(800, 600)
glutCreateWindow(b"DDA Line Drawing using PyOpenGL")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
