class Solution(object):
    def main(self):
        import sys

        chars = list(sys.stdin.readline().rstrip())
        stack = [0]
        count = 0
        popped = False
        for char in chars:
            if stack[-1] == 0: 
                stack.append(char)
                popped = False
            elif stack[-1] == "(":
                if char == "(":
                    stack.append(char)
                    popped = False
                else:
                    stack.pop()
                    if popped:
                        count += 1
                    else:
                        count += len(stack) - 1
                        popped = True
        print(count)

if __name__ == "__main__":
    Solution().main()
