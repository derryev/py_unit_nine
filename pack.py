
from dog import Dog


class Pack:

    def __init__(self, leader):
        self.members = [leader]
        self.leader_index = 0

    def get_leader_name(self):
        return self.members[self.leader_index].get_name()

    def add_member(self, new_member):
        self.members.append(new_member)

    def print_pack(self):
        print("The dog pack contains:")
        for member in self.members:
            print(member.get_name())

    def new_leader(self, new_leader_number):
        greatest_member_index = len(self.members) - 1
        old_leader_name = str(self.members[self.leader_index].get_name())
        if new_leader_number != self.leader_index and new_leader_number <= greatest_member_index:
            self.leader_index = new_leader_number
            new_leader_name = str(self.members[self.leader_index].get_name())
            print(new_leader_name+" deposes "+old_leader_name+" as the leader of the pack.")
        else:
            print("That is not a valid dog.")

    def all_sit(self):
        for member in self.members:
            member.sit()

    def all_lay_down(self):
        for member in self.members:
            member.lay_down()

    def all_cook_dinner(self):
        for member in self.members:
            member.cook_dinner()

    def all_print_tricks(self):
        for member in self.members:
            member.print_trick_list()

    def __str__(self):
        leader_name = str(self.members[self.leader_index].get_name())
        return f"Pack: The leader of the dog pack is {self.get_leader_name()}. There are "+str(len(self.members))+" dogs in the pack."


dog1 = Dog("Spot")
dog2 = Dog("Buc")
dog3 = Dog("Gus")

pack1 = Pack(dog1)
pack1.add_member(dog2)
pack1.add_member(dog3)
pack1.print_pack()
print(pack1.get_leader_name())
pack1.new_leader(1)
print(pack1.get_leader_name())
pack1.all_sit()
pack1.all_print_tricks()
dog1.cook_dinner()
pack1.all_print_tricks()
print(pack1)
print(dog1)
