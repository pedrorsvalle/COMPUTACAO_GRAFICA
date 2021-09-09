
###                                  Bandeira Argentina                                           ###

from sys import builtin_module_names
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 


def Desenharquadrado(**args):
    glColor3f(args['r'],args['g'],args['b'])
    glBegin(GL_QUADS)
    glVertex2f(args ['x1'],args['y1'])
    glVertex2f(args ['x2'],args['y2'])
    glVertex2f(args ['x3'],args['y3'])
    glVertex2f(args ['x4'],args['y4'])
    glEnd()

def Desenhar():
        byte = 255
        tam_x = 850
        tam_y = 400
        glClear(GL_COLOR_BUFFER_BIT)
        Desenharquadrado( x1=-375 /tam_x, y1 = 290/tam_y, x2=375/tam_x, y2 = 290/tam_y, x3 = 375/tam_x, y3 =50/tam_y, x4 = -375/tam_x, y4 = 0/tam_y,  r =(0/byte) , g= (0/byte) ,b = (255/byte))
        Desenharquadrado( x1= -375/tam_x, y1 = 80/tam_y, x2 = 375/tam_x, y2 = 80/tam_y, x3=375/tam_x, y3= -124/tam_y, x4= -375/tam_x, y4 = -124/tam_y, r = (255/byte), g = (255/byte), b = (255/byte))
        Desenharquadrado( x1= -375/tam_x, y1 = -20/tam_y, x2 = 375/tam_x, y2 = -20/tam_y, x3 = 375/tam_x, y3 = -200/tam_y, x4 = -375/tam_x, y4 =-200/tam_y,   r = (0/byte), g =(0/byte), b = (255/byte))
        glFlush()

    

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(850,400)
glutInitWindowPosition(0,0)
glutCreateWindow(b'ddd')
glutDisplayFunc(Desenhar)
glClearColor(1,1,1,1)
glutMainLoop()

