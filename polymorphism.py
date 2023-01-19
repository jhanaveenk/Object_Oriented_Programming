class Polygon:
    def render(self):
        print("Rendering Polygon...")


class Square(Polygon):
    def render(self):
        print("rendering Square...")


class Circle(Polygon):
    def render(self):
        print("rendering circle...")


s1 = Square()
s1.render()

s2=Circle()
s2.render()