class Solution(object):
    def __init__(self):
        import sys
        _, self.count = map(int, sys.stdin.readline().rstrip().split(" "))
        self.numbers = list(map(int, list(sys.stdin.readline().rstrip())))

    def main(self):
        stack = []
        count = 0
        for number in self.numbers:
            if len(stack) == 0 or stack[-1] >= number:
                if len(stack) < len(self.numbers) - self.count:
                    stack.append(number)
            else:
                while count < self.count and stack[-1] < number:       
                    stack.pop()
                    count += 1
                    if len(stack) == 0:
                        break
                stack.append(number)
        number = "".join(map(str, stack))
        print(number)


if __name__ == "__main__":
    Solution().main()
