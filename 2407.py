class Solution(object):
    def __init__(self):
        import sys
        self.input_value = list(
            map(int, sys.stdin.readline().rstrip().split(" ")))

    def ncr(self, n, m):
        if n == m:
            return 1
        n_fac = self.factorial(n)
        m_fac = self.factorial(m)
        n_minus_m_fac = self.factorial(n - m)
        return n_fac // (m_fac * n_minus_m_fac)

    def factorial(self, n):
        if n == 0:
            return 1
        res = n
        for i in range(n - 1, 0, -1):
            res *= i
        return res

    def main(self):
        n, m = self.input_value
        print(self.ncr(n, m))


if __name__ == "__main__":
    Solution().main()
