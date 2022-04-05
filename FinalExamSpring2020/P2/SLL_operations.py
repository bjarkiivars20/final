
from itertools import count


class SLL_Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.data == other.data

# IMPLEMENT HERE
"""
 if h1.next == None and h2.next == None:
        return False
    if count_recursion <= 2:
        if h1.data != h2.data:
            return False
        else:
            count_recursion += 1
            return doubled_recur(h1.next, h2, count_recursion)
    else:
        count_recursion = 1
        return doubled_recur(h1, h2.next, count_recursion)

"""

def doubled_recur(h1, h2) -> bool:
    if h1 == None:
        return True
    if h2 == h1.next: #I am using the eq operator in the SLL_Node
        if h1.next.next == None and h1.next.data != h2.data:
            return False
        return doubled_recur(h1.next.next, h2.next)
    return False
        

def is_doubled(head1, head2):
    if head1.data != None and head2.data != None:
        return doubled_recur(head1, head2)
    return False

if __name__ == "__main__":
    
    print("\n\nTESTING DOUBLED:\n")

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(7, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4)))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9,             SLL_Node(4))))
    print(is_doubled(head1, head2))

    head1 = SLL_Node(4, SLL_Node(4, SLL_Node(6, SLL_Node(6, SLL_Node(9, SLL_Node(9, SLL_Node(4, SLL_Node(4))))))))
    head2 = SLL_Node(4,             SLL_Node(6,             SLL_Node(9)))
    print(is_doubled(head1, head2))
