from dataclasses import dataclass

@dataclass
class Pizza:
    size: int
    cheese: bool
    pepperoni: bool
    mushrooms: bool
    onions: bool
    bacon: bool

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self
    
    def set_pepperoni(self, pepperoni):
        self.pizza.pepperoni = pepperoni
        return self
    
    def set_mushrooms(self, mushrooms):
        self.pizza.mushrooms = mushrooms
        return self
    
    def set_onions(self, onions):
        self.pizza.onions = onions
        return self
    
    def set_bacon(self, bacon):
        self.pizza.bacon = bacon
        return self

    def build(self):
        return self.pizza

class PizzaDirector:
    def __init__(self):
        self.builder = PizzaBuilder()
    
    def make_pizza(self, size, cheese, pepperoni, mushrooms, onions, bacon):
        return(self.builder.set_size(size).set_cheese(cheese).set_pepperoni(pepperoni).set_mushrooms(mushrooms).set_onions(onions).set_bacon(bacon).build())