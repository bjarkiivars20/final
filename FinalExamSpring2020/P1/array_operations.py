
class Array:
    def __init__(self, arr, count):
        self.capacity = 4
        while self.capacity < count:
            self.capacity *= 2
        self.arr = [None] * self.capacity
        for i in range(count):
            self.arr[i] = arr[i]
        self.size = count

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        for i in range(self.size):
            ret_str += str(self.arr[i]) + " "
        return ret_str

    def contains(self, val):
        for index in range(self.size):
            if self.arr[index] == val:
                return True
        return False

    def remove(self, index):
        for i in range(index, (self.size - 1)):
            self.arr[i] = self.arr[(i + 1)] #Þá dettur indexinn út sem við sendum inn
        self.size -= 1

    def remove_all(self, other):
        remove_count = 0
        index = 0

        while index < self.size:
            if other.contains(self.arr[index]):
                self.remove(index)
                remove_count += 1
            else:
                index += 1

        return remove_count


"""
Removes all items from the array that have the same value as any of the values in the other 
array.  The remaining items must not have gaps between them in the array and must retain their 
order. 
The operation then returns an integer with the number of items removed. 
The final 5% are rewarded for solutions that only go once through the array and for each item 
in the array only at most once through the other array. 
Time complexity: O(n*m) where n is the length of self and m is the length of other.

NOTE: expected output = 
COUNT:        6
REMAINING:    1 6 7 8 3
"""


if __name__ == "__main__":
    arr1 = Array([1, 4, 2, 6, 5, 4, 5, 5, 7, 8, 3, None, None, None, None, None], 11)
    print(arr1)
    print(len(arr1))
    print(arr1.contains(7))
    print(arr1.contains(9))
    removed_count = arr1.remove_all(Array([2, 5, 4, None], 3))
    print(removed_count)
    print(arr1)
    print(len(arr1))