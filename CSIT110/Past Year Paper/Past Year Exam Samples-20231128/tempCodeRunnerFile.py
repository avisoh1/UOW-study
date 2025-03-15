class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_dict(cls, arg):
        return cls(arg["name"], arg["price"])
    
