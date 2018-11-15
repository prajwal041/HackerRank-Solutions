n=int(input())
lis = list(map(int,input().strip().split()))[:n]
maxi = max(lis)
while max(lis)==maxi:
    lis.remove(max(lis))
print(max(lis))



# Alternate Solution
# li = sorted(input().split())
# maxi = li[::-1]
#
# print(maxi[1])