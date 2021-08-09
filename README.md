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
