n = int(input())
integer_list = map(int, input().split())
in_list = [int(x) for x in integer_list]
print(in_list)
t = tuple(in_list)
print(hash(t))
