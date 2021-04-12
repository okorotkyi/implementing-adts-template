# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Stack-LL
#
# NAME:         Oleksandr Korotkyi
# ASSIGNMENT:   Technical HW: Implementing ADTs
#pytest StackLL_test.py

from Node import Node

class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        if list is not None:
            for item in list:
                self.add(item)

    def peek(self):
        if self.is_empty():
          return None
        else:
          return self.top.get_data()

    def pop(self):
      if self.is_empty():
        return None
      else:
        top = self.top
        self.top = self.top.get_next()
        return top.get_data()

    def push(self, data=None):
        new_node = Node(data, self.top)
        self.top = new_node

    def print(self):
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return self.top == None

    def clear(self):
      while not self.is_empty():
        self.top == None
        self.top = self.top.get_next()

def main():
    s = StackLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.push(i)
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    while not s.is_empty():
        print(s.pop())

# Don't run main on import
if __name__ == "__main__":
    main()

