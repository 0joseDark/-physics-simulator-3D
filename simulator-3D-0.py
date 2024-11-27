from ursina import *

class Simulador3D(Entity):
    def __init__(self):
        super().__init__()
        self.cubos = []  # Lista para armazenar os cubos criados

    def criar_cubo(self, position):
        """
        Cria um novo cubo na posição especificada.
        """
        novo_cubo = Entity(
            model='cube',  # Modelo de cubo
            color=color.random_color(),  # Cor aleatória
            position=position
        )
        self.cubos.append(novo_cubo)

def atualizar():
    """
    Atualiza o comportamento do simulador.
    """
    if held_keys['w']:  # Avançar
        camera.position += Vec3(0, 0, 0.1)
    if held_keys['s']:  # Recuar
        camera.position -= Vec3(0, 0, 0.1)
    if held_keys['a']:  # Mover para a esquerda
        camera.position -= Vec3(0.1, 0, 0)
    if held_keys['d']:  # Mover para a direita
        camera.position += Vec3(0.1, 0, 0)
    if held_keys['q']:  # Subir
        camera.position += Vec3(0, 0.1, 0)
    if held_keys['e']:  # Descer
        camera.position -= Vec3(0, 0.1, 0)

# Inicialização do aplicativo Ursina
app = Ursina()

# Criação do terreno base
chao = Entity(
    model='plane', 
    scale=10, 
    color=color.green, 
    collider='box'
)

# Criação do simulador
simulador = Simulador3D()

# Adiciona cubo inicial no centro
simulador.criar_cubo((0, 0.5, 0))

# Controle de clique para adicionar cubos
def input(key):
    if key == 'left mouse down':
        # Adiciona um novo cubo na posição do rato
        nova_posicao = mouse.world_point
        if nova_posicao:
            nova_posicao = (round(nova_posicao.x), 0.5, round(nova_posicao.z))
            simulador.criar_cubo(nova_posicao)

# Inicia o loop principal
app.run()
