from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import choice

brown_1 = [250/255, 229/255, 211/255]
brown_2 = [240/255, 178/255, 122/255]
brown_3 = [230/255, 126/255, 34/255]
brown_4 = [175/255, 96/255, 26/255]
brown_5 = [120/255, 66/255, 18/255]

brown_range = [brown_1, brown_2, brown_3, brown_4, brown_5]
dark_brown_range = [brown_3, brown_4, brown_5]

def draw_colored_cube(color):
    """
    Dibuja un cubo sólido con el color RGB indicado.
    """
    glColor3fv(color)
    glutSolidCube(1)

def solid_face_xz(x_size, z_size, colors):
    """
    Crea una cara sólida rectangular en el plano XZ,
    utilizando cubos de los colores indicados.
    """
    for x in range(x_size):
        for z in range(z_size):
            glPushMatrix()
            glTranslatef(x, 0, z)
            draw_colored_cube(choice(colors))
            glPopMatrix()

def solid_circle_face_xz(x_size, z_size, radius, colors):
    """
    Dibuja una cara circular en el plano XZ usando cubos,
    dentro del radio especificado.
    """
    for x in range(x_size):
        for z in range(z_size):
            if (z <= radius and (x - radius)**2 + (z - radius)**2 < radius**2):
                glPushMatrix()
                glTranslatef(x, 0, z)
                draw_colored_cube(choice(colors))
                glPopMatrix()

def empty_face_xz(x_size, z_size, colors):
    """
    Dibuja solo el borde (contorno) de una cara rectangular en el plano XZ.
    """
    for x in range(x_size - 1):
        glPushMatrix()
        glTranslatef(x, 0, 0)
        draw_colored_cube(choice(colors))
        glPopMatrix()

    for z in range(z_size - 1):
        glPushMatrix()
        glTranslatef(x_size - 1, 0, z)
        draw_colored_cube(choice(colors))
        glPopMatrix()

    for x in reversed(range(x_size - 1)):
        glPushMatrix()
        glTranslatef(x, 0, z_size - 1)
        draw_colored_cube(choice(colors))
        glPopMatrix()

    for z in reversed(range(z_size)):
        glPushMatrix()
        glTranslatef(0, 0, z)
        draw_colored_cube(choice(colors))
        glPopMatrix()

def empty_pipe_y(x_size, y_size, z_size, colors):
    """
    Construye una estructura hueca vertical (tipo tubo) apilando bordes rectangulares.
    """
    for y in range(y_size):
        glPushMatrix()
        glTranslatef(0, y, 0)
        empty_face_xz(x_size, z_size, colors)
        glPopMatrix()

def mesa_solida(ancho, largo):
    """
    Dibuja una mesa completa: tablero superior, cuatro patas huecas
    y decoraciones redondeadas en los extremos.
    """
    if (ancho < 9) or (largo < 9):
        print("Error en los parámetros de mesa_solida")
        return

    alto = 10       
    grosor = 3     
    radius = ancho / 2  

    
    glPushMatrix()
    glTranslatef(0, alto, 0)
    solid_face_xz(ancho, largo, brown_range)
    glPopMatrix()

    
    glPushMatrix()
    glTranslatef(1, 0, 1)
    empty_pipe_y(grosor, alto, grosor, dark_brown_range)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(ancho - grosor - 2, 0, 1)
    empty_pipe_y(grosor, alto, grosor, dark_brown_range)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(ancho - grosor - 2, 0, largo - grosor - 2)
    empty_pipe_y(grosor, alto, grosor, dark_brown_range)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1, 0, largo - grosor - 2)
    empty_pipe_y(grosor, alto, grosor, dark_brown_range)
    glPopMatrix()

 
    glPushMatrix()
    glTranslatef(0, alto, -ancho // 2)
    solid_circle_face_xz(ancho, ancho, radius, brown_range)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, alto, largo + radius)
    glRotatef(180, 1, 0, 0)
    solid_circle_face_xz(ancho, ancho, radius, brown_range)
    glPopMatrix()
