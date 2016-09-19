class Visitor(object):
    """
    visitor for binary tree
    """
    def visit(self, node):
        return getattr(self, "visit_" + type(node).__name__)(node)
    def visit_BiNode(self, node):
        print("visiting binode")
        op = node.op
        leftval = self.visit(node.leftchild)
        rightval = self.visit(node.rightchild)

        if op == "+":
            return leftval + rightval
        if op == "-":
            return leftval - rightval
        if op == "*":
            return leftval * rightval


    def visit_Number(self, node):
        print("visiting number")
        return int(node.value)