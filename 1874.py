class Solution(object):
    def __init__(self):
        import sys
        n = int(sys.stdin.readline().rstrip())
        self.series = []
        for _ in range(n):
            self.series.append(int(sys.stdin.readline().rstrip()))

    def main(self):
        stack = [0]
        track = []
        res = []
        num = 1
        length = len(self.series)
        while len(self.series) > 0 and num <= length + 1:
            if stack[-1] > self.series[0]:
                stack.pop()
                track.append("-")
            elif stack[-1] < self.series[0]:
                stack.append(num)
                num += 1
                track.append("+")
            else:
                res.append(stack.pop())
                self.series.pop(0)
                track.append("-")
        if len(res) < length:
            print("NO")
        else:
            print(*track, sep="\n")

if __name__ == "__main__":
    Solution().main()
