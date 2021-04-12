# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 5: Queue-Array
#
# NAME:         Oleksandr Korotkyi
# ASSIGNMENT:   Technical HW: Implementing ADTs
# pytest QueueArray_test.py

class QueueArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.front = -1 
        self.tail = -1

    def get_front(self):
        if self.is_empty():
          return None
        else:
          return self.array[self.front] 

    def get_tail(self):
        if self.is_empty():
          return None
        else:
          return self.array[self.tail] 

    def deq(self):
      if self.is_empty():
        return None
      else: 
        temp = self.array[self.front]
        print(self.array)
        if self.tail > 1 :
          self.array = self.array[1:self.tail] 
        else:
          self.array = self.array[:0] 
          self.front = -1
        self.tail -= 1
        return temp

    def enq(self, data):
        if self.is_empty():
          self.front = 0
          self.tail = 0
          self.array[0] = data
          return
        if self.is_full():
          new_array = [None for i in range(self.size() + 1)]
          size = self.size()
          for i in range(size):
            x = i + self.front 
            new_array[i] = self.array[x % len(self.array)] 
          self.array = new_array
          self.front = 0
          self.tail = size - 1
        self.tail += 1
        self.array[self.tail % len(self.array)] = data
        
    def print(self):
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        self.array = self.array[:0]
        self.front = -1
        self.tail = -1

    def is_full(self):
        l = self.size()
        return l >= len(self.array)

    def size(self):
        if self.front == -1:
            return 0
        l = self.tail - self.front + 1
        if self.tail < self.front:
            l = len(self.array) - self.front + self.tail + 1
        return l


def main():
    s = QueueArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 4):
        s.enq(i)
        #print("Size:", s.size())
        #s.print()
    s.print()
    print("Deq: ", s.deq())
    print("Deq: ", s.deq())
    s.print()
    for i in range(5, 11):
        s.enq(i)
        #print("Size:", s.size())
        #s.print()
    print("Front:", s.get_front())
    print("Tail: ", s.get_tail())
    print("Deq:  ", s.deq())
    s.print()
    print("Is empty?", s.is_empty())
    print("Size:", s.size())


# Don't run main on import
if __name__ == "__main__":
    main()
