

class Dog:
    def __init__(self, dog_name):
        self.dog_name = dog_name
        self.trick_list = []

    def get_name(self):
        return self.dog_name

    def sit(self):
        print(self.dog_name+" sits.")
        self.trick_list.append("sit")

    def lay_down(self):
        print(self.dog_name+" lays down.")
        self.trick_list.append("lay down")

    def cook_dinner(self):
        print(self.dog_name+" cooks a gourmet, three-course dinner.")
        self.trick_list.append("cook dinner")

    def print_trick_list(self):
        if self.trick_list == []:
            print(self.dog_name + " has not performed any tricks yet.")
        else:
            print(self.dog_name, "has performed the following tricks:")
            for trick in self.trick_list:
                print(trick)


dog1 = Dog("Spot")
dog1.sit()
dog1.lay_down()
dog1.cook_dinner()
dog1.print_trick_list()

dog2 = Dog("Gus")
dog2.cook_dinner()
dog2.print_trick_list()

dog3 = Dog("Buc")
dog3.print_trick_list()