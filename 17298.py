class Solution(object):
    def __init__(self):
        import sys
        _ = sys.stdin.readline()
        self.numbers = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    def main(self):
        stack = []
        result = [0] * len(self.numbers)
        self.numbers.reverse()
        for i, number in enumerate(self.numbers):
            if len(stack) == 0:
                stack.append(number)
                result[i] = -1
            else:
                while stack[-1] <= number:
                    stack.pop()
                    if len(stack) == 0:
                        break
                result[i] = stack[-1] if len(stack) > 0 else -1
                stack.append(number)
        result.reverse()
        print(*result, sep=" ")


if __name__ == "__main__":
    Solution().main()
