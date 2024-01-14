class Customer:
    
    def __init__(self, id, pin, name):
        self.id = id
        self.pin = pin
        self.name = name

    def match(self, pin):
        return self.pin == pin

