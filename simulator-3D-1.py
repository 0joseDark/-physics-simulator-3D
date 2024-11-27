from ursina import *

# Inicialização do aplicativo Ursina
app = Ursina()

# Criando o terreno
ground = Entity(
    model='plane',       # Modelo do chão
    texture='white_cube', # Textura padrão
    scale=(10, 1, 10),   # Escala do chão
    color=color.green,   # Cor do chão
    collider='box'       # Colisor para interação
)

# Criando a lista de cubos para serem renderizados
cubos = []

# Função para criar cubos
def criar_cubo(posicao):
    """
    Cria um cubo na posição especificada.
    """
    novo_cubo = Entity(
        model='cube',         # Modelo básico do cubo
        color=color.random_color(), # Cor aleatória
        scale=1,              # Escala do cubo
        position=posicao,     # Posição no espaço 3D
        collider='box'        # Colisor para detectar interações
    )
    cubos.append(novo_cubo)

# Adicionando o cubo inicial
criar_cubo((0, 0.5, 0))

# Controle de interação via teclado e rato
def input(key):
    """
    Lida com as entradas do rato e teclado.
    """
    if key == 'left mouse down':  # Clique do rato
        if mouse.world_point:  # Pega o ponto clicado no mundo 3D
            posicao = mouse.world_point
            posicao = Vec3(round(posicao.x), 0.5, round(posicao.z))  # Alinha à grade
            criar_cubo(posicao)

# Atualizando a posição da câmera com o teclado
def update():
    """
    Atualiza a posição da câmera com base nas teclas pressionadas.
    """
    velocidade = 5 * time.dt  # Velocidade de movimento (ajustável)
    if held_keys['w']:  # Avançar
        camera.position += Vec3(0, 0, velocidade)
    if held_keys['s']:  # Recuar
        camera.position -= Vec3(0, 0, velocidade)
    if held_keys['a']:  # Mover para a esquerda
        camera.position -= Vec3(velocidade, 0, 0)
    if held_keys['d']:  # Mover para a direita
        camera.position += Vec3(velocidade, 0, 0)
    if held_keys['q']:  # Subir
        camera.position += Vec3(0, velocidade, 0)
    if held_keys['e']:  # Descer
        camera.position -= Vec3(0, velocidade, 0)

# Configurações da câmera
camera.position = Vec3(0, 10, -20)  # Posição inicial da câmera
camera.rotation_x = 30              # Inclinação inicial da câmera

# Inicia o aplicativo
app.run()
