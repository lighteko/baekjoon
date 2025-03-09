import sys


class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, array):
        self.root = Node("ROOT")
        self.length = 0
        self.cursor = self.root
        for char in array:
            node = Node(char)
            self.cursor.next = node
            node.prev = self.cursor
            self.cursor = node
            self.length += 1
        self.end = Node("")
        self.end.prev = self.cursor
        self.cursor.next = self.end
        self.cursor = self.end
        
    
    def insert_left(self, value):
        temp = self.cursor.prev
        node = Node(value)
        self.cursor.prev = node
        node.prev = temp
        temp.next = node
        node.next = self.cursor
        self.length += 1
    
    def remove_left(self):
        if self.root is self.cursor.prev:
            return
        temp = self.cursor.prev.prev
        self.cursor.prev.prev = None
        self.cursor.prev.next = None
        self.cursor.prev.value = None
        temp.next = self.cursor
        self.cursor.prev = temp
        self.length += 1

    def print_all(self):
        self.cursor = self.root.next
        while self.cursor.next:
            print(self.cursor.value, end="")
            self.cursor = self.cursor.next

class Solution(object):
    def __init__(self):
        self.string = sys.stdin.readline().rstrip()
        m = int(sys.stdin.readline().rstrip())
        self.command_list = [sys.stdin.readline().rstrip() for _ in range(m)]

    def execute(self, string, command_list):
        text = LinkedList(list(string))
        for command in command_list:
            if command[0] == "L":
                if text.cursor != text.root.next:
                    text.cursor = text.cursor.prev
            elif command[0] == "D":
                if text.cursor != text.end:
                    text.cursor = text.cursor.next
            elif command[0] == "B":
                if text.cursor != text.root.next:
                    text.remove_left()
            elif command[0] == "P":
                operand = command[-1]
                text.insert_left(operand)
        text.print_all()

    def main(self):
        self.execute(self.string, self.command_list)


if __name__ == "__main__":
    Solution().main()
