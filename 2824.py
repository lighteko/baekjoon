from sys import stdin
from functools import reduce

class Solution:
    def __init__(self):
        self.n = int(stdin.readline().rstrip())
        self.a_list = list(map(int, stdin.readline().rstrip().split()))
        self.m = int(stdin.readline().rstrip())
        self.b_list = list(map(int, stdin.readline().rstrip().split()))
        
        self.limit = 10**6
        self.primes = self.sieve(self.limit)

    def sieve(self, n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = False
        return [i for i in range(2, n + 1) if prime[i]]

    def factorizer(self, num):
        factors = {}
        for prime in self.primes:
            if prime * prime > num:  
                break
            while num % prime == 0:
                factors[prime] = factors.get(prime, 0) + 1
                num //= prime
        if num > 1:  
            factors[num] = factors.get(num, 0) + 1
        return factors

    def gcd(self, a_list, b_list):
        a_factors = {}
        b_factors = {}

        for num in a_list:
            for key, val in self.factorizer(num).items():
                a_factors[key] = a_factors.get(key, 0) + val

        for num in b_list:
            for key, val in self.factorizer(num).items():
                b_factors[key] = b_factors.get(key, 0) + val

        res = 1
        for key in a_factors:
            if key in b_factors:
                res *= key ** min(a_factors[key], b_factors[key])

        return str(res) if len(str(res)) < 9 else str(res)[-9:]

    def main(self):
        print(self.gcd(self.a_list, self.b_list))

if __name__ == "__main__":
    Solution().main()
