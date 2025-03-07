class Solution(object):
    def __init__(self):
        import sys
        self.lotto = []
        while True:
            string = sys.stdin.readline().rstrip().split(" ")
            numbers = list(map(int, string))[1:]
            self.lotto.append(numbers)
            if not numbers:
                break

    def print_combinations(self, index, numbers, picked=[]):
        length = len(numbers)
        if len(picked) == 6:
            print(*picked)
            return
        for i in range(index, length):
            self.print_combinations(i + 1, numbers, [*picked, numbers[i]])

    def main(self):
        for i, lotto_numbers in enumerate(self.lotto):
            if not lotto_numbers:
                return
            self.print_combinations(0, lotto_numbers)
            if i < len(self.lotto) - 2:
                print()


if __name__ == "__main__":
    Solution().main()
