import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from physics_simulator import PhysicsSimulator, Cube, Vector3D

# Inicializar o simulador de física
simulator = PhysicsSimulator(gravity=Vector3D(0, -9.8, 0), time_step=0.02)

# Configuração inicial dos cubos
cubes = [
    Cube(position=Vector3D(0, 5, 0), size=Vector3D(1, 1, 1), mass=1),
    Cube(position=Vector3D(2, 5, 0), size=Vector3D(1, 1, 1), mass=1),
]
for cube in cubes:
    simulator.add_object(cube)

# Configurações da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

def init_window():
    """Inicializa a janela 3D com PyGame e OpenGL."""
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
    gluPerspective(45, (WINDOW_WIDTH / WINDOW_HEIGHT), 0.1, 50.0)
    glTranslatef(0.0, -3.0, -10)

def draw_cube(cube):
    """Desenha um cubo no OpenGL."""
    glPushMatrix()
    glTranslate(cube.position.x, cube.position.y, cube.position.z)
    glBegin(GL_QUADS)
    for face in [
        (-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1),
        (1, -1, -1), (1, -1, 1), (1, 1, 1), (1, 1, -1)
    ]:
        glVertex3fv(face)
    glEnd()
    glPopMatrix()

def handle_input():
    """Gerencia as entradas do teclado e do rato."""
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        glTranslatef(0, 0, 0.5)
    if keys[K_s]:
        glTranslatef(0, 0, -0.5)
    if keys[K_a]:
        glTranslatef(0.5, 0, 0)
    if keys[K_d]:
        glTranslatef(-0.5, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == MOUSEBUTTONDOWN:
            # Adicionar novos cubos com o botão do rato
            if event.button == 1:  # Botão esquerdo
                new_cube = Cube(
                    position=Vector3D(0, 5, 0), size=Vector3D(1, 1, 1), mass=1
                )
                simulator.add_object(new_cube)

def main():
    """Função principal."""
    init_window()
    clock = pygame.time.Clock()

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Atualizar física
        simulator.step()

        # Desenhar todos os cubos
        for cube in simulator.objects:
            draw_cube(cube)

        handle_input()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
