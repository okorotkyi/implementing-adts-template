# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Queue-LL
#
# NAME:         Oleksandr Korotkyi
# ASSIGNMENT:   Technical HW: Implementing ADTs
# pytest QueueLL_test.py

from Node import Node

class QueueLL(object):
    def __init__(self, list=None):
        self.front = None
        self.tail = None
        if list is not None:
            for item in list:
                self.enq(item)

    def get_front(self):
      if self.is_empty():
        return None
      else:
        print (self.front.get_data())
        return self.front.get_data()

    def get_tail(self):
      if self.is_empty():
        return None
      else:
        return self.tail.get_data()

    def deq(self):
        if self.is_empty():
          return None
        else:
          temp = self.front
          self.front = None
          return temp.get_data()

    def enq(self, data):
        if self.is_empty():
          self.tail = Node(data)
          self.front = self.tail
        else:
          new_node = Node(data, self.tail)
          self.tail = new_node

    def print(self):
        n = self.front
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return self.tail == None

    def clear(self):
        self.tail = None



def main():
    s = QueueLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.enq(i)
    s.print()
    print("Peek:", s.peek())
    print("Deq: ", s.deq())
    s.print()
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

