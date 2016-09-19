class BiNode(object):
    """
    representing operator node object
    """
    def __init__(self):
        self.op = ""
        self.leftchild = None
        self.rightchild = None

    def add_child(self, child):
        if self.leftchild == None:
            self.leftchild = child
        else:
            self.rightchild = child

    def get_child(self):
        if self.rightchild != None:
            return self.rightchild
        return self.leftchild
