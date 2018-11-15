# list = []
# list.insert(0,5)
# list.insert(1,10)
# list.insert(0,6)
# print(list)
#
# list.remove(6)
# list.append(9)
# list.append(1)
# list.sort()
# print(list)
# list.pop()
# list.reverse()
# print(list)

n = input()
l = []
for _ in range(int(n)):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)