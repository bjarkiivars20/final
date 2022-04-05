
#IMPORTANT NOTE: Each operator can only have TWO operands, like AND(T, F) or OR(T, T).. etc
# IMPLEMENT HERE
class BoolNode:
    def __init__(self, token = None, left = None, right = None):
        self.token = token
        self.left = left
        self.right = right

class BooleanTree:
    def __init__(self):
        self.root = None
    
    def build_recur(self,statement_list):
        if statement_list[0] == "OR" or statement_list[0] == "AND":
            node = BoolNode(statement_list[0])
            statement_list.pop(0)
            node.left = self.build_recur(statement_list)
            node.right = self.build_recur(statement_list)
            return node
        else:
            node = BoolNode(statement_list[0])
            statement_list.pop(0)
            return node

    def build_tree(self, statement_string):
        statement_list = statement_string.replace("(", " ").replace(")", " ").replace(",", " ").split()
        self.root = self.build_recur(statement_list)


    def get_root_value_recur(self, node):
        if node.token == "OR":
            return self.get_root_value_recur(node.left) or self.get_root_value_recur(node.right)
        elif node.token == "AND":
            return self.get_root_value_recur(node.left) and self.get_root_value_recur(node.right)
        elif node.token == "T":
            return True
        elif node.token == "F":
            return False

    def get_root_value(self):
        return self.get_root_value_recur(self.root)

        

if __name__ == "__main__":

    print("\nSHOWING HOW TO LOSE THE DELIMITERS, IF WANTED")
    statement_string = "OR(AND(T,F),F)"
    print(statement_string)
    # YOU CAN DO THIS IN YOUR build_tree() OPERATION IF THE LIST FORMAT FEELS BETTER
    statement_list = statement_string.replace("(", " ").replace(")", " ").replace(",", " ").split()
    print(statement_list)


    print("\n\nTESTING BOOLEAN TREE\n")

    # THESE TESTS SHOULD WORK EXACTLY AS THEY ARE BUT FEEL FREE TO MAKE MORE EXTENSIVE TESTS AS WELL

    bt = BooleanTree()
    statement_string = "OR(AND(T,F),F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "OR(T,AND(T,F))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "OR(AND(T,T),F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(T,OR(F,F))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(OR(F,T),T)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(F,F)"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())
    statement_string = "AND(OR(OR(F,F),T),OR(T,AND(T,F)))"
    print(statement_string)
    bt.build_tree(statement_string)
    print(bt.get_root_value())