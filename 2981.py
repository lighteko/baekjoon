from sys import stdin
from functools import reduce


class Solution:
    def __init__(self):
        n = int(stdin.readline().rstrip())
        self.n_list = [int(stdin.readline().rstrip()) for _ in range(n)]

    def find_m(self, n_list):
      difference = []
      n_list.sort()
      for i in range(len(n_list) - 1):
          difference.append(n_list[i + 1] - n_list[i])
      res = reduce(self.euclidean_gcd, difference)
      for i in range(2, res + 1):
          if res % i == 0:
              print(i, end=" ")

    def euclidean_gcd(self, a, b):
        if b == 0: return a
        return self.euclidean_gcd(b, a % b)

    def main(self):
        self.find_m(self.n_list)

if __name__ == "__main__":
    Solution().main()
