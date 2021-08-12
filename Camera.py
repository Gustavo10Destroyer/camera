from Game import Game

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
        if type(x) == tuple or type(x) == list:
            return self.relative(screen, x[0], x[1])
        elif type(x) == dict:
            if "x" in x and "y" in x:
                return self.relative(screen, x["x"], x["y"])
            elif "X" in x and "Y" in x:
                return self.relative(screen, x["X"], x["Y"])
            else:
                raise TypeError("Invalid dict position!")
        
        width = screen.get_width()
        height = screen.get_height()

        position = self.position
        anchorX = self.anchorPoint["x"]
        anchorY = self.anchorPoint["y"]

        return (width * anchorX) + x - position["x"], (height * anchorY) + y - position["y"]
    
    def worldToScreen(self, screen, *args):
        if type(args) == list or type(args) == tuple:
            if type(args[0]) == tuple:
                return self.worldToScreen(screen, args[0][0], args[0][1])
            elif type(args[0]) == dict:
                if "x" in args[0] and "y" in args[0]:
                    return self.worldToScreen(screen, args[0]["x"], args[0]["y"])
                elif "X" in args[0] and "Y" in args[0]:
                    return self.worldToScreen(screen, args[0]["X"], args[0]["Y"])
                else:
                    raise TypeError("Invalid dict position!")
        elif type(args) == dict:
            if "x" in args and "y" in args:
                return self.worldToScreen(screen, args["x"], args["y"])
            elif "X" in args and "Y" in args:
                return self.worldToScreen(screen, args["X"], args["Y"])
            else:
                raise TypeError("Invalid dict position!")
        
        width = screen.get_width()
        height = screen.get_height()

        anchorX = self.anchorPoint["x"]
        anchorY = self.anchorPoint["y"]

        x = (args[0] + (width * anchorX)) - self.position["x"]
        y = (args[1] + (height * anchorY)) - self.position["y"]

        onScreen = False

        if x < width:
            onScreen = True
        elif y < height:
            onScreen = True
        
        return (x, y), onScreen