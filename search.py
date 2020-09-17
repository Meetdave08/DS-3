# 3031varun
class Search:
    def __init__(self, lst, ele):
        self.lst = lst
        self.ele = ele

    def binary_search(self):
        sorted_lst = sorted(self.lst)
        start = 0
        end = len(sorted_lst) - 1
        while start <= end:
            mid = (end + start) // 2
            if sorted_lst[mid] < self.ele:
                start = mid + 1
            elif sorted_lst[mid] > self.ele:
                end = mid - 1
            else:
                return mid
        return False

    def linear_search(self):
        for i in range(len(self.lst)):
            if self.lst[i] == self.ele:
                return i
        return False


if __name__ == '__main__':
    test_list = [35, 10, 43, 82, 66, 51, 97]
    test_value_1 = 43
    test_value_2 = 44
    test_search = Search(test_list, test_value_1)
    print(test_search.binary_search())
    print(test_search.linear_search())
    test_search_2 = Search(test_list, test_value_2)
    print(test_search_2.binary_search())
    print(test_search_2.linear_search())
