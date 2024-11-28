class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
        
    def set_name(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age
    
    def display(self):
        return '{} {}'.format(self.name, self.age)