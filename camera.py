class Camera:
    def __init__(self, Width, Height):
        self.X = 0
        self.Y = 0
        self.AnchorX = 0.5
        self.AnchorY = 0.5
        self.Width = Width
        self.Height = Height
    
    def anchorPoint(self, X, Y):
        self.AnchorX = X
        self.AnchorY = Y

    def translate(self, X, Y):
        self.X = X
        self.Y = Y
    
    def worldToScreen(self, X, Y):
        nX = (X + (self.Width * self.AnchorX)) - (self.Width / 2)
        nY = (Y + (self.Height * self.AnchorY)) - (self.Height / 2)

        onScreen = False

        if nX < self.Width:
            onScreen = True
        elif nY < self.Height:
            onScreen = True
        
        return (nX, nY), onScreen

    def relative(self, X, Y):
        return (self.Width * self.AnchorX) + X - self.X, (self.Height * self.AnchorY) + Y - self.Y