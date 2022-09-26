## Reorder data in logfiles 
## https://leetcode.com/problems/reorder-data-in-log-files/


import re

class SortLogs:
    def __init__(self):
       pass

    def reverseOrder(self, my_list):
        final_list = []
        for element in my_list:
            elements = element.split(' ')
            final_list.append(elements[-1] + ' ' + ' '.join(elements[0:-1]))
        print(final_list)
        return final_list


    def reorderLogFiles(self, logs):
        digits = []
        letters = []
        for element in logs:
            key, log_content = element.split(' ', 1)
            if re.match("^[a-z]", log_content, re.I):
                letters.append(log_content + ' ' + key)
            else:
                digits.append(log_content + ' ' + key)
        my_reversed_letters = self.reverseOrder(sorted(set(letters)))
        my_reversed_digits =  self.reverseOrder(sorted(set(digits)))
        return  my_reversed_letters + my_reversed_digits



if __name__ == '__main__':
    logs = ["dig3 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(logs)
    sort_logs = SortLogs()

    print(sort_logs.reorderLogFiles(logs))
