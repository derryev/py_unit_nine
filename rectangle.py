class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = ""
        self.perimeter = ""

    def calculate_perimeter(self):
        self.perimeter = (self.width*2)+(self.height*2)
        return self.perimeter

    def calculate_area(self):
        self.area = (self.width*self.height)
        return self.area
