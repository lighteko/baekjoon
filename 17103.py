import sys


class Solution(object):
    def __init__(self):
        n = int(sys.stdin.readline().rstrip())
        self.cases = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
        self.primes = [True] * 1_000_001
        self.sieve()

    def sieve(self):
        self.primes[0] = self.primes[1] = False
        for i in range(2, int(1_000_001 ** 0.5) + 1):
            if self.primes[i]:
                for j in range(i * i, 1_000_001, i):
                    self.primes[j] = False

    def goldbach_partitions(self, n):
        count = 0
        for i in range(2, n // 2 + 1):
            if self.primes[i] and self.primes[n - i]:
                count += 1
        return count

    def main(self):
        for case in self.cases:
            print(self.goldbach_partitions(case))


if __name__ == "__main__":
    Solution().main()
