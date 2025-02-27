class Solution(object):
    def __init__(self):
        import sys
        self.n_list = []
        while True:
            n = int(sys.stdin.readline().rstrip())
            if n == 0:
                break
            self.n_list.append(n)

    def is_prime(self, num):
        for i in range(2, num):
            if i * i > num:
                break
            if num % i == 0:
                return False
        return num != 1
    
    def count_primes(self, n):
        counter = 0
        for i in range(n + 1, 2*n + 1):
            if self.is_prime(i):
                counter += 1
        return counter

    def main(self):
        for n in self.n_list:
            print(self.count_primes(n))

if __name__ == "__main__":
    Solution().main()
