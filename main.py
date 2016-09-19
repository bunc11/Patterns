


def main():

    eq = "(9+(9-(2+6)))*((3*2)*(1+3))"
    tb = TreeBuilder()
    tree = tb.build_tree(eq)

    print(Visitor().visit(tree))

if __name__ == '__main__':
    from treebuilder import *
    from visitor import *
    main()