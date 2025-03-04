class Solution(object):
    def __init__(self):
        import sys
        self.n_list = []
        self.prime = [True] * (1_000_001)
        self.prime[0] = self.prime[1] = False
        while True:
            n = int(sys.stdin.readline().rstrip())
            if n == 0:
                break
            self.n_list.append(n)
        self.sieve()

    def goldbach(self, n): 
        for i in range(3, int(n / 2) + 1, 2):
            if self.prime[i] and self.prime[n - i]:
                return f"{n} = {min(i, n - i)} + {max(i, n - i)}"
        return "Goldbach's conjecture is wrong."
    
    def sieve(self):
        for i in range(2, int(1_000_000 ** 0.5) + 1):
            if self.prime[i]:
                for j in range(i * i, 1_000_001, i):
                    self.prime[j] = False
    
    def main(self):
        for n in self.n_list:
            print(self.goldbach(n))

if __name__ == "__main__":
    Solution().main()
