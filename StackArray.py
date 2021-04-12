# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Stack-Array
#
# NAME:         Oleksandr Korotkyi
# ASSIGNMENT:   Technical HW: Implementing ADTs
# pytest StackArray_test.py

class StackArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.top = -1

    def peek(self):
        if self.is_empty():
          return None
        else:
          return self.array[self.top]

    def pop(self):
        if self.is_empty():
          return None
        else:
          top = self.array[self.top]
          self.array[self.top] = None
          self.top -= 1
          return top

    def push(self, data):
        if self.is_empty():
          self.top = 0
          self.array[self.top] = data
        elif self.is_full():
          new_array = [None for i in range(2 * self.size())]
          size = self.size()
          for i in range(size):
            x = i + self.top 
            new_array[i] = self.array[x % len(self.array)] 
          self.array = new_array
          self.top += 1
          self.array[self.top] = data
        else:
          self.top += 1
          self.array[self.top] = data

    def print(self):
        for i in range(self.top, -1, -1):
            print(self.array[i], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.top == len(self.array) - 1

    def clear(self):
        self.array = self.array[:0]
        self.top = -1

    def size(self):
        return self.top + 1


def main():
    s = StackArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 10):
        s.push(i)
    s.print()
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()

