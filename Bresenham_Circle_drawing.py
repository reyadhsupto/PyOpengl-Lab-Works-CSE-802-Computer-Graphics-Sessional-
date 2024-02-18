from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to draw a point
def drawPoint(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Function to draw a circle using Bresenham's circle drawing algorithm
def drawCircleBresenham(radius, xc, yc):
    x = 0
    y = radius
    d = 3 - 2 * radius

    while x <= y:
        drawPoint(xc + x, yc + y)
        drawPoint(xc - x, yc + y)
        drawPoint(xc + x, yc - y)
        drawPoint(xc - x, yc - y)
        drawPoint(xc + y, yc + x)
        drawPoint(xc - y, yc + x)
        drawPoint(xc + y, yc - x)
        drawPoint(xc - y, yc - x)

        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white

    # Circle parameters
    radius = 50
    xc, yc = 100, 100

    drawCircleBresenham(radius, xc, yc)

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
glutCreateWindow(b"Bresenham Circle Drawing using PyOpenGL")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
