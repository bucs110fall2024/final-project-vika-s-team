from src.Animal import Animal

class Panda(Animal):
    def __init__(self, x, y, name="Panda"):
        """
        initializes panda object

        Args:
            x (int): x position of panda
            y (int): y position of panda
            name (str): names the panda "Panda"
        """
        super().__init__(x, y, name, "assets/panda.png", 250)
        self.rect.topleft = (x, y)