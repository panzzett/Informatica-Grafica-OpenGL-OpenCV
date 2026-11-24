from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

angle = 0

def init():
  glClearColor(0.1, 0.1, 0.1, 1)
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_LIGHTING)
  glEnable(GL_LIGHT0)
  
  light_pos = [1.0, 5.0, 5.0, 1.0]
  glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

  glEnable(GL_COLOR_MATERIAL)
  glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

def draw_lamp():
  quad = gluNewQuadric()

  # Base circular
  glColor3f(0.7, 0.7, 0.7)
  glPushMatrix()
  glTranslatef(0.0, 0.0, 0.0)
  glRotatef(-90, 1, 0, 0)
  gluDisk(quad, 0.0, 0.5, 32, 1)
  glPopMatrix()

  # Tubo vertical
  glColor3f(0.9, 0.9, 0.9)
  glPushMatrix()
  glTranslatef(0.0, 0.0, 0.0)
  glRotatef(-90, 1, 0, 0)
  gluCylinder(quad, 0.05, 0.05, 2.0, 16, 16)
  glPopMatrix()

  # Pantalla cónica (tipo tulipa)
  glColor3f(1.0, 0.9, 0.6)
  glPushMatrix()
  glTranslatef(0.0, 2.0, 0.0)
  glRotatef(-90, 1, 0, 0)
  gluCylinder(quad, 0.4, 0.25, 0.6, 32, 1)  # pantalla
  glPopMatrix()

  # Tapa superior de la pantalla
  glColor3f(0.8, 0.7, 0.5)
  glPushMatrix()
  glTranslatef(0.0, 2.6, 0.0)
  glRotatef(-90, 1, 0, 0)
  gluDisk(quad, 0.0, 0.25, 32, 1)  # círculo superior
  glPopMatrix()

  # Bombilla
  glColor3f(1.0, 1.0, 0.8)
  glPushMatrix()
  glTranslatef(0.0, 2.3, 0.0)
  glutSolidSphere(0.1, 16, 16)  # bombilla
  glPopMatrix()

def display():
  global angle
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glLoadIdentity()
  gluLookAt(3, 2, 5, 0, 1, 0, 0, 1, 0)

  glRotatef(angle, 0, 1, 0)
  draw_lamp()

  glutSwapBuffers()

def reshape(width, height):
  glViewport(0, 0, width, height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(45, width / float(height), 1, 100)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()

def timer(v):
  global angle
  angle += 1
  glutPostRedisplay()
  glutTimerFunc(16, timer, 0)

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  glutInitWindowSize(800, 600)
  glutCreateWindow(b"Lampara de salon - Modelo 3D")
  init()
  glutDisplayFunc(display)
  glutReshapeFunc(reshape)
  glutTimerFunc(16, timer, 0)
  glutMainLoop()

if __name__ == "__main__":
  main()
