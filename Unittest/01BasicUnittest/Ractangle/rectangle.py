class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width * self.height)*2