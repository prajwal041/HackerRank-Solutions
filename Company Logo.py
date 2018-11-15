from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]




#### Solution in dictionary
# def char_frequency(string):
#     dict = {}
#     for i in string:
#         keys = dict.keys()
#         if i in keys:
#             dict[i]+=1
#         else:
#             dict[i]=1
#     return dict
#
# string = input()
# print(char_frequency(string))

