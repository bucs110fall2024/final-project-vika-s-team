from src.Animal import Animal

class Snake(Animal):
    def __init__(self, x, y, name="Snake"):
        """
        initializes snake object

        Args:
            x (int): x positon of snake
            y (int): y position of snake
            name (str): name of the snake as "Snake"
        """
        super().__init__(x, y, name, "assets/snake.png", 250)
        self.rect.topleft = (x, y)