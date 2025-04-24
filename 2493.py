class Solution(object):
    def __init__(self):
        import sys
        _ = sys.stdin.readline()
        self.towers = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    def main(self):
        stack = []
        result = [0] * len(self.towers)
        for i, tower in enumerate(self.towers):
            if len(stack) == 0:
                stack.append((i + 1, tower))
            else:
                while stack[-1][1] < tower:
                    stack.pop()
                    if len(stack) == 0:
                        break
                result[i] = stack[-1][0] if len(stack) > 0 else 0
                stack.append((i + 1, tower))
        print(*result, sep=" ")


if __name__ == "__main__":
    Solution().main()
