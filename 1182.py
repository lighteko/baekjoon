class Solution(object):
    def __init__(self):
        import sys
        _, self.s = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        self.numbers = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    
    def find_subsets(self, ls):
        if len(ls) == 1:
            return [ls, []]
        subsets = self.find_subsets(ls[1:])
        temp = list(subsets)
        for elem in temp:
            subsets.append(elem + [ls[0]])
        return subsets

    def main(self):
        subsets = self.find_subsets(self.numbers)
        subsets.remove([])
        sums = list(map(sum, subsets))
        count = len(list(filter(lambda x: x == self.s, sums)))
        print(count)


if __name__ == "__main__":
    Solution().main()
