
class node:
    def __init__(self):
        self.value = None
        self.next = None


class Linked_List_Selection_Sort:
    def __init__(self):
        self.first = None
    
    def insert(self, val):
        if not self.first:
            self.first = node()
            self.first.value = val
            self.first.next = None
        else:
            temp = self.first
            while (temp.next):
                temp = temp.next
            temp.next = node()
            temp = temp.next
            temp.value = val
            temp.next = None
    def display(self):
        temp = self.first
        str_print = ''
        while (temp):
            assert isinstance(temp, node)
            str_print += str(temp.value) + ' '
            temp = temp.next
        print(str_print)
    
    def selection_sort(self):
        beg = self.first
        minimum = self.first
        while (beg.next):
            minimum = beg
            current = beg.next
            while current:
                if (current.value < minimum.value):
                    minimum = current
                current = current.next
            t = beg.value
            beg.value = minimum.value
            minimum.value = t
            beg = beg.next
        

if __name__ == '__main__':
    linked_list = Linked_List_Selection_Sort()
    linked_list.insert(1)
    linked_list.insert(8)
    linked_list.insert(5)
    linked_list.insert(4)
    linked_list.insert(9)
    linked_list.insert(2)
    print("Before sorting : ")
    linked_list.display()
    linked_list.selection_sort()
    print("After Sorting : ")
    linked_list.display()
