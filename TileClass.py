class TileClass:

    status = False
    number = -1

    def __init__(self, number, image, background, x, y, size, canvas) -> None:
        self.image = image
        self.background = background
        self.x = x
        self.y = y
        self.size = size
        self.canvas = canvas
        self.number = number

    def click(self):
        self.status = True

    def draw(self):
        if self.status and self.number != -1:
            self.canvas.create_image(self.x, self.y, image=self.image[self.number-1])
        elif self.number != -1:
            self.canvas.create_image(self.x, self.y, image=self.background)