def createRect(camera, old_rect):
    def rect(surface, draw_type, *args):
        origin = (args[1].left, args[1].top)

        if draw_type == camera.GLOBAL_DRAW:
            (args[1].left, args[1].top) = camera.relative(surface, origin[0], origin[1])
        elif draw_type == camera.SCREEN_DRAW:
            pass

        old_rect(surface, *args)
        (args[1].left, args[1].top) = origin
    
    return rect

def createCircle(camera, old_circle):
    def circle(surface, draw_type, *args):
        newArgs = []

        for arg in args:
            newArgs.append(arg)
        
        if draw_type == camera.GLOBAL_DRAW:
            newArgs[1] = camera.relative(surface, args[1][0], args[1][1])
        elif draw_type == camera.SCREEN_DRAW:
            pass
        else:
            raise TypeError("Invalid draw type!")

        old_circle(surface, *newArgs)
    
    return circle

class Camera:
    def __init__(self, pygame):
        self.GLOBAL_DRAW = "global_draw"
        self.SCREEN_DRAW = "screen_draw"

        self.position = {
            "x": 0,
            "y": 0
        }

        self.anchorPoint = {
            "x": 0,
            "y": 0
        }

        pygame.camera = self
        pygame.draw.rect = createRect(self, pygame.draw.rect)
        pygame.draw.circle = createCircle(self, pygame.draw.circle)
    
    def relative(self, screen, x, y):
        width = screen.get_width()
        height = screen.get_height()

        position = self.position
        anchorX = self.anchorPoint["x"]
        anchorY = self.anchorPoint["y"]

        return (width * anchorX) + x - position["x"], (height * anchorY) + y - position["y"]
    
    def worldToScreen(self, screen, *args):
        if type(args[0]) == tuple:
            return self.worldToScreen(screen, *args)
        
        width = screen.get_width()
        height = screen.get_height()

        anchorX = self.anchorPoint["x"]
        anchorY = self.anchorPoint["y"]
        
        x = (args[0] + (width * anchorX)) - (width * anchorX)
        y = (args[1] + (height * anchorY)) - (height * anchorY)

        onScreen = False

        if x < width:
            onScreen = True
        elif y < height:
            onScreen = True
        
        return (x, y), onScreen