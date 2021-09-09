

###                                  Bandeira Argentina                                           ###

from sys import builtin_module_names
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 

global windowWidth,windowHeight,a1,b1,rsize,xstep,ystep

a1 = 100.0
b1 = 150.0
rsize = 50                                                

#Tamanho do incremento nas direções x e y 
#(número de pixels para se mover a cada
#intervalo de tempo)
xstep = 1.0
ystep = 1.0



def Desenharquadrado(**args):
    glColor3f(args['r'],args['g'],args['b'])
    glBegin(GL_QUADS)
    glVertex2f(args ['x1'],args['y1'])
    glVertex2f(args ['x2'],args['y2'])
    glVertex2f(args ['x3'],args['y3'])
    glVertex2f(args ['x4'],args['y4'])
    glEnd()

def Desenhar():
    
        global windowWidth,windowHeight,a1,b1,rsize,xstep,ystep

        byte = 255
        tam_x = 850
        tam_y = 400
        glClear(GL_COLOR_BUFFER_BIT)
        Desenharquadrado( x1=-375 /tam_x, y1 = 290/tam_y, x2=375/tam_x, y2 = 290/tam_y, x3 = 375/tam_x, y3 =50/tam_y, x4 = -375/tam_x, y4 = 0/tam_y,  r =(0/byte) , g= (0/byte) ,b = (255/byte))
        Desenharquadrado( x1= -375/tam_x, y1 = 80/tam_y, x2 = 375/tam_x, y2 = 80/tam_y, x3=375/tam_x, y3= -124/tam_y, x4= -375/tam_x, y4 = -124/tam_y, r = (255/byte), g = (255/byte), b = (255/byte))
        Desenharquadrado( x1= -375/tam_x, y1 = -20/tam_y, x2 = 375/tam_x, y2 = -20/tam_y, x3 = 375/tam_x, y3 = -200/tam_y, x4 = -375/tam_x, y4 =-200/tam_y,   r = (0/byte), g =(0/byte), b = (255/byte))
        glFlush()

# Executa os comandos OpenGL
glutSwapBuffers()
        
def Timer(value):

   global windowWidth,windowHeight,a1,b1,rsize,xstep,ystep
   # Muda a direção quando chega na borda esquerda ou direita
   if(a1 > windowWidth-rsize or a1 < 0):
            xstep = -xstep

   # Muda a direção quando chega na borda superior ou inferior
   if(b1 > windowHeight-rsize or b1 < 0):
          ystep = -ystep
          
   # Verifica as bordas.  Se a window for menor e o 
   # quadrado sair do volume de visualização 
   if(a1 > windowWidth-rsize):
         a1 = windowWidth-rsize-1

   if(b1 > windowHeight-rsize):
         b1 = windowHeight-rsize-1


   # Move o quadrado
   a1 += xstep
   b1 += ystep





 # Redesenha o quadrado com as novas coordenadas 
   glutPostRedisplay()
   glutTimerFunc(33,Timer, 1)
    
# Inicializa parâmetros de rendering
def Inicializa():   
    glClearColor(0.0, 0.0, 0.0, 1.0)#; // Define a cor de fundo da janela de visualização como preta

def AlteraTamanhoJanela(w, h):
    global windowWidth,windowHeight,a1,b1,rsize,xstep,ystep
    # Evita a divisao por zero
    if(h == 0):
        h = 1
                           
    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)

    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Estabelece a janela de seleção (left, right, bottom, top)     
    if (w <= h):
        windowHeight = 250.0*h/w
        windowWidth = 250.0
    else:
        windowWidth = 250.0*w/h
        windowHeight = 250.0

    #windowWidth = w
    #windowHeight = h
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)
    

#// Programa Principal 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(850,400);
    glutInitWindowPosition(0,0);
    glutCreateWindow(b"ddd");
    glutDisplayFunc(Desenhar);
    #glutReshapeFunc(AlteraTamanhoJanela);
    glutTimerFunc(33, Timer, 1);
    #Inicializa();
    glutMainLoop();

main()





#glutInit(sys.argv)
#glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
#glutInitWindowSize(850,400)
#glutInitWindowPosition(0,0)
#glutCreateWindow(b'ddd')
#glutDisplayFunc(Desenhar)
#glClearColor(1,1,1,1)
#glutMainLoop()

