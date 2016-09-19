from number import *
from binode import *

class TreeBuilder(object):
    """
    builds tree from simple string equation
    """
    def __init__(self):
        self.root = BiNode()
        self.temp = self.root
        self.stack = []

    def build_tree(self, eq):


        for char in eq:
            print("char " + char)
            if char == "(":
                print("adding binode")
                self.temp.add_child(BiNode())
                self.stack.append(self.temp)
                self.temp = self.temp.get_child()
            elif char == ")":
                print("go up")
                self.temp = self.stack.pop()
            elif char in ["+", "-", "*", "/"]:
                print("set op")
                self.temp.op = char
            else:
                print("add number")
                self.temp.add_child(Number(char))


        return self.root