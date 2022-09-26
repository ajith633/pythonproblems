from collections import Counter


class ThresholdCounter:
    def __init__(self, threshold):
        self.threshold = threshold

    def process_log(self, list_of_lists):
        result = []
        ret_list = []
        for list in list_of_lists:
            result.append(list[0])
            result.append(list[1])
        my_result =  Counter(result)
        for key,value in my_result.items():
            if value >= self.threshold:
                 ret_list.append(key)
        return ret_list

    @staticmethod
    def some_method(str):
        print(str)


if __name__ == '__main__':
    lists = [
        [345366,89921,45],
        [29323,38239,23],
        [38239,345366,15],
        [29323,38239,77],
        [345366,38239,23],
        [29323,345366,13],
        [38239,38239,23]
	]
    t = ThresholdCounter(3)
    x = ThresholdCounter(4)
    print(t.process_log(lists))
    print(x.process_log(lists))
    t.some_method("hello")
