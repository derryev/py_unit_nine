class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.perimeter = ""
        self.area = ""

    def calculate_perimeter(self):
        self.perimeter = self.side1+self.side2+self.side3
        return self.perimeter

    def calculate_area(self):
        s = self.perimeter/2
        self.area = (s(s-self.side1)(s-self.side2)(s-self.side3))**.5
        return self.area