# Use Stack to hold each group
class Stack:
    def __init__(self):
        self.arr = []
    
    def is_empty(self):
        return len(self.arr) == 0

    def push(self, value):
        self.arr.append(value)
        return

    def pop(self):
        if self.is_empty():
            return None
        return self.arr.pop()


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
    
    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user_input,group_input):
    if user_input == "" or user_input == None or group_input == None \
        or not isinstance(user_input,str) or not isinstance(group_input,Group):
        print("Usage: is_user_in_group(user_input as str type, group_input as Group type))")
        return False

    stack = Stack()
    stack.push(group_input)
    while not stack.is_empty():
        current_group = stack.pop()
        for user in current_group.get_users():
            if user == user_input:
                return True
        for group in current_group.get_groups():
            stack.push(group)
    
    return False

# Main part of the program
parent = Group("parent")
child = Group("child")
child2 = Group("child2")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(child2)

print(is_user_in_group("sub_child_user",child2))