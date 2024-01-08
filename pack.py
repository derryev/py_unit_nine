
from dog import Dog


class pack:
    def __init__(self, leader):
        self.members = [leader]
        self.leader_index = 0

    def get_leader_name(self):
        return self.members[self.leader_index].get_name()

    def add_member(self, new_member):
        self.members.append(new_member)

    def print_pack(self):
        for member in self.members:
            print(member.get_name())


pack1 = pack("dog1")
pack1.add_member("dog2")
pack1.add_member("dog3")
pack1.print_pack()
