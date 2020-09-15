# 3031varun
class ListOperations:
    def __init__(self, lst):
        self.lst = lst

    def binary_search(self, ele):
        sorted_lst = self.bubble_sort()
        start = 0
        end = len(sorted_lst) - 1
        while start <= end:
            mid = (end + start) // 2
            if sorted_lst[mid] < ele:
                start = mid + 1
            elif sorted_lst[mid] > ele:
                end = mid - 1
            else:
                return mid
        return False

    def linear_search(self, ele):
        for i in range(len(self.lst)):
            if self.lst[i] == ele:
                return i
        return False

    def bubble_sort(self):
        sorted_lst = self.lst.copy()
        for i in range(len(sorted_lst) - 1):
            for j in range(0, len(sorted_lst) - i - 1):
                if sorted_lst[j] > sorted_lst[j + 1]:
                    sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
        return sorted_lst

    def selection_sort(self):
        sorted_lst = self.lst.copy()
        for i in range(len(sorted_lst)):
            min_idx = i
            for j in range(i + 1, len(sorted_lst)):
                if sorted_lst[min_idx] > sorted_lst[j]:
                    min_idx = j
            sorted_lst[i], sorted_lst[min_idx] = sorted_lst[min_idx], sorted_lst[i]
        return sorted_lst

    def insertion_sort(self):
        sorted_lst = self.lst.copy()
        for i in range(1, len(sorted_lst)):
            key = sorted_lst[i]
            j = i - 1
            while j >= 0 and key < sorted_lst[j]:
                sorted_lst[j + 1] = sorted_lst[j]
                j -= 1
            sorted_lst[j + 1] = key
        return sorted_lst

    def merge(self, lst_2):
        merged_lst = self.lst.copy()
        for e in lst_2:
            merged_lst.append(e)
        return merged_lst

    def reverse(self):
        reversed_lst = []
        for i in reversed(range(0, len(self.lst))):
            reversed_lst.append(self.lst[i])
        return reversed_lst


if __name__ == "__main__":
    test_list = [35, 10, 43, 82, 66, 51, 97]
    test_list_2 = [11, 36, 44, 52, 67, 83, 98]
    test_value_1 = 43
    test_value_2 = 44
    object_1 = ListOperations(test_list)
    object_2 = ListOperations(test_list)
    binary_result_1 = object_1.binary_search(test_value_1)
    print(binary_result_1)
    binary_result_2 = object_2.binary_search(test_value_2)
    print(binary_result_2)
    linear_result_1 = object_1.linear_search(test_value_1)
    print(linear_result_1)
    linear_result_2 = object_2.linear_search(test_value_2)
    print(linear_result_2)
    bubble_sort = object_1.bubble_sort()
    print(bubble_sort)
    selection_sort = object_1.selection_sort()
    print(selection_sort)
    insertion_sort = object_1.insertion_sort()
    print(insertion_sort)
    merge = object_1.merge(test_list_2)
    print(merge)
    reverse = object_1.reverse()
    print(reverse)
