class Solution(object):
    def __init__(self):
        import sys
        input_values = sys.stdin.readline().rstrip().split(" ")
        self.m, self.n = int(input_values[0]), int(input_values[1])

    def is_prime(self, num):
        for i in range(2, num):
            if i * i > num:
                break
            if num % i == 0:
                return False
        return num != 1

    def main(self):
        for i in range(self.m, self.n + 1):
            if self.is_prime(i):
                print(i)


if __name__ == "__main__":
    Solution().main()
