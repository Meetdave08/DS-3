class Search:
    def __init__(self, lst, ele):
        self.lst = sorted(lst)
        self.ele = ele

    def binary(self):
        low = 0
        high = len(self.lst) - 1
        while low <= high:
            mid = (high + low) // 2
            if self.lst[mid] < self.ele:
                low = mid + 1
            elif self.lst[mid] > self.ele:
                high = mid - 1
            else:
                return mid
        return False

    def linear(self):
        for i in range(len(self.lst)):
            if self.lst[i] == self.ele:
                return i
        return False


if __name__ == "__main__":
    test_list = [10, 35, 43, 51, 66, 82, 97]
    test_value_1 = 43
    test_value_2 = 44
    test_search_1 = Search(test_list, test_value_1)
    test_search_2 = Search(test_list, test_value_2)
    binary_result_1 = test_search_1.binary()
    print(binary_result_1)
    binary_result_2 = test_search_2.binary()
    print(binary_result_2)
    linear_result_1 = test_search_1.linear()
    print(linear_result_1)
    linear_result_2 = test_search_2.linear()
    print(linear_result_2)


