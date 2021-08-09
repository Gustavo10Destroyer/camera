# camera

Como obter a posição da Câmera
```python
from camera import Camera

width = 600
height = 300

camera = Camera(width, height)

X = camera.X # Posição da câmera em relação ao eixo X
Y = camera.Y # Posição da câmera em relação ao eixo Y

print(X) # 0
print(Y) # 0
```

Métodos da Câmera
```python
from camera import Camera

width = 600
height = 300

camera = Camera(width, height)

X = 100
Y = 100

NPC_X = 0
NPC_Y = 0

camera.translate(X, Y) # Transforma o X e Y na posição inicial, o que dá o efeito de movimento...
NPC_POS = camera.relative(NPC_X, NPC_Y) # Calcula a posição do objeto no mundo, em relação com a posição da Câmera | (100, 100)
camera.worldToScreen(NPC_POS[0], NPC_POS[1]) # Transforma a posição global(no mundo) para posição do objeto na tela
```

# translate(X, Y)
```python
from camera import Camera

width = 600
height = 300

camera = Camera(width, height)

X = 100
Y = 100

camera.translate(X, Y)
```
Define a posição da câmera, não retorna nada

# relative(X, Y)
```python
from camera import Camera

width = 600
height = 300

camera = Camera(width, height)

X = 100
Y = 100

position = (0, 0)

camera.translate(X, Y)
position = camera.relative(position[0], position[1])

print(position) # (400, 250)
```
Calcula a posição global(no mundo) em relação à posição da Câmera + (Tamanho * AnchorPoint), retorna uma tupla com X e Y

# anchorPoint(anchorX, anchorY)
```python
from camera import Camera

width = 600
height = 300

camera = Camera(width, height)

anchorX = 0.5
anchorY = 0.5

camera.anchorPoint(anchorX, anchorY) # None
```
Define o ponto de ancoragem, o calculo é o seguinte (width * anchorX) (height * anchorY), então 0.5 deixa a posição da câmera no centro da tela
