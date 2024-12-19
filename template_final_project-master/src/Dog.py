from src.Animal import Animal

class Dog(Animal):
    """
    creates the dog image and name
    """
    def __init__(self, x, y, name="Dog"):
        self.x = x
        self.y = y
        super().__init__(x, y, name, "assets/dog_3.png",250)