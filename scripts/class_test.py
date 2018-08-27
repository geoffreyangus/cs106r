class foo():
    def __init__(self):
        self.x = 5
    def get_x(self):
        return self.x
    def add_10(self):
        self.x += 10

y = foo()
z = y.get_x()
y.add_10()
print(z)
