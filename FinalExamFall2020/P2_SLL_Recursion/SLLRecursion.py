class sll_node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

##########################   helper functions are encouraged in these problems   ##########################
def assume_desc_recur(node:sll_node) -> bool:
    if node == None:
        return True
    elif node.next != None:
        if node.value < node.next.value:
            return False
    return assume_desc_recur(node.next)

def assume_asc_recur(node):
    if node == None:
        return True
    elif node.next != None:
        if node.value > node.next.value:
            return False
    return assume_asc_recur(node.next)

def is_asc_desc_ordered(head):
    if head.next.value > head.value: #if the value after head is bigger then that of the head, we assume ASC order
        ret_bool = assume_asc_recur(head.next)
        return ret_bool
    elif head.next.value < head.value: #if the value of the head is bigger then that of the head, we assume DESC order
        ret_bool = assume_desc_recur(head.next)
        return ret_bool
    else: #If the next node after head is equals to that of the head, it's neither asc or desc, so return false
        return False
    

def count_series_recur(node, series = 0):
    if node == None:
        return series
    elif node.next != None:
        if node.value > node.next.value:
            series += 1
    else:
        series += 1
    return count_series_recur(node.next, series)

def count_ascending_series(head):
    series = count_series_recur(head)
    return series


if __name__ == "__main__":
    print("is_asc_desc_ordered tests:")
    test_head = sll_node(1, sll_node(2, sll_node(3, None))) #1,2,3
    print(is_asc_desc_ordered(test_head))
    test_head = sll_node(3, sll_node(2, sll_node(1, None))) #3,2,1
    print(is_asc_desc_ordered(test_head))
    test_head = sll_node(1, sll_node(3, sll_node(2, None))) #1,3,2
    print(is_asc_desc_ordered(test_head))

    print("\ncount_ascending_series tests:")
    test_head = sll_node(1, sll_node(2, sll_node(3, None))) #1,2,3
    print(count_ascending_series(test_head))
    test_head = sll_node(3, sll_node(2, sll_node(1, None))) #3,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(2, sll_node(3, sll_node(2, sll_node(3, sll_node(4, sll_node(2, sll_node(7, sll_node(8, None))))))))) #1,2,3,2,3,4,2,7,8
    print(count_ascending_series(test_head))
    test_head = sll_node(5, sll_node(4, sll_node(3, sll_node(2, sll_node(1, None))))) #5,4,3,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(1, sll_node(1, sll_node(2, sll_node(1, None))))) #1,1,1,2,1
    print(count_ascending_series(test_head))
    test_head = sll_node(1, sll_node(2, sll_node(1, sll_node(4, sll_node(5, sll_node(6, sll_node(1, sll_node(7, sll_node(1, None)))))))))
    print(count_ascending_series(test_head)) #1, 2, 1, 4, 5, 6, 1, 7, 1 -> 1 1 1 1 4 series
