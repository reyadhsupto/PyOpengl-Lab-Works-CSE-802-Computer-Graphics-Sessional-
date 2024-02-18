from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to draw a point
def drawPoint(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def bresenham(x1, y1, x2, y2): 
  
    m_new = 2 * (y2 - y1) 
    slope_error_new = m_new - (x2 - x1) 
  
    y = y1 
    for x in range(x1, x2+1): 
        drawPoint(x, y)
  
        # Add slope to increment angle formed 
        slope_error_new = slope_error_new + m_new 
  
        # Slope error reached limit, time to 
        # increment y and update slope error. 
        if (slope_error_new >= 0): 
            y = y+1
            slope_error_new = slope_error_new - 2 * (x2 - x1)
            
            
# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white

    # Coordinates of two points
    x1, y1 = 10, 12
    x2, y2 = 30, 35

#     drawLineBresenham(x1*10, y1*10, x2*10, y2*10)
    bresenham(x1*10, y1*10, x2*10, y2*10)

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
glutCreateWindow(b"Bresenham Line Drawing using PyOpenGL")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
