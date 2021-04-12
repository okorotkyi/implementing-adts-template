# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Linked List
#
# NAME:         Oleksandr Korotkyi
# ASSIGNMENT:   Technical HW: Implementing ADTs
# pytest LinkedList_test.py
from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

    def get_head(self):
        return self.head.get_data()

    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def search(self, data):
      node = self.head
      while node != None:
        if node.get_data() == data:
          return True
        node = node.get_next()
      return False

    def delete(self, data):
      node = self.head
      prev = None
      while node != None:
        if node.get_data() == data:
          if prev == None:
            self.head = node.get_next()
          else:
            prev.set_next(node.get_next())
          return node.get_data()
        prev = node
        node = node.get_next()
      return None

    def print(self):
        n = self.head
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return self.head == None

    def clear(self):
        self.head = None

def main():
    l = list(range(1, 5))
    l.reverse()
    ll = LinkedList(l)
    ll.print()
    print("Search 4: ", ll.search(4))
    print("Search 5: ", ll.search(5))
    print("Delete 5: ", ll.delete(5))
    print("Delete 4: ", ll.delete(4))
    ll.print()
    print("Delete 1: ", ll.delete(1))
    ll.print()

# Don't run main on import
if __name__ == "__main__":
    main()

