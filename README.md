# camera

Variáveis da Câmera
# position
- Dict com duas chaves, x e y, que representam a posição da câmera

# anchorPoint
- Dict com duas chaves, x e y, que representam o ponto de ancoragem da câmera (positionX + (width * anchorX)) (positionY + (height * anchorY))

# GLOBAL_DRAW
- Variável para definir o tipo de desenho global, com os calculos de câmera aplicados

# SCREEN_DRAW
- Tipo de desenho na tela, sem os calculos de câmera, serve para elementos estáticos

Métodos da Câmera
# relative(x, y)
```python
import pygame
from camera import Camera

pygame.init()

camera = Camera(pygame)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 300])

camera.anchorPoint["x"] = 0.5 # Set X camera point to center
camera.anchorPoint["y"] = 0.5 # Set Y camera point to center

running = True

COLOR = (0, 255, 0)
POSITION = (0, 0)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  print(pygame.camera == camera) # True
  pygame.draw.circle(screen, camera.GLOBAL_DRAW, COLOR, POSITION)
  
  pygame.display.update()
  
  clock.tick(30)

pygame.quit()
```
