from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Tamaño inicial de ventana
width, height = 800, 800

def init():
    glClearColor(0.1, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    light_pos = [1.0, 5.0, 5.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

def draw_sofa():
    glPushMatrix()
    # Base del asiento
    glColor3f(0.6, 0.3, 0.0)
    glPushMatrix()
    glTranslatef(0, 0.25, 0)
    glScalef(2, 0.5, 2)
    glutSolidCube(1)
    glPopMatrix()

    # Respaldo
    glColor3f(0.4, 0.2, 0.0)
    glPushMatrix()
    glTranslatef(0, 1.0, -0.75)
    glScalef(2, 1.5, 0.5)
    glutSolidCube(1)
    glPopMatrix()

    # Reposabrazos izquierdo
    glColor3f(0.5, 0.25, 0.1)
    glPushMatrix()
    glTranslatef(-1.0, 0.75, 0)
    glScalef(0.5, 1.0, 2)
    glutSolidCube(1)
    glPopMatrix()

    # Reposabrazos derecho
    glPushMatrix()
    glTranslatef(1.0, 0.75, 0)
    glScalef(0.5, 1.0, 2)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

def set_projection(viewport_id):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    if viewport_id == 1:
        # Ortogonal
        glOrtho(-4, 4, -4, 4, -10, 10)
    elif viewport_id == 2:
        # Gabinete (oblicua)
        glOrtho(-4, 4, -4, 4, -10, 10)
        shear = [
            1, 0, -0.5, 0,
            0, 1, -0.5, 0,
            0, 0,    1, 0,
            0, 0,    0, 1
        ]
        glMultMatrixf(shear)
    elif viewport_id == 3:
        # Perspectiva simétrica
        gluPerspective(60, 1.0, 1.0, 20.0)
    elif viewport_id == 4:
        # Perspectiva oblicua
        gluPerspective(45, 1.0, 1.0, 20.0)


def set_viewport(viewport_id):
    w2, h2 = width // 2, height // 2
    if viewport_id == 1:
        glViewport(0, h2, w2, h2)
    elif viewport_id == 2:
        glViewport(w2, h2, w2, h2)
    elif viewport_id == 3:
        glViewport(0, 0, w2, h2)
    elif viewport_id == 4:
        glViewport(w2, 0, w2, h2)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for i in range(1, 5):
        set_viewport(i)
        set_projection(i)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        if i in [3, 4]:  # perspectivas
            gluLookAt(5, 5, 5, 0, 0.5, 0, 0, 1, 0)
        else:  # proyecciones paralelas
            glTranslatef(0, -0.5, -5)

        draw_sofa()

    glutSwapBuffers()

def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, width, height)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Sillon con Proyecciones 3D")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
