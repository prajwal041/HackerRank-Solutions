from itertools import combinations

string,n = input().split()
for i in range(1, int(n)+1):
    for j in combinations(sorted(string),i):
        print("".join(j))


