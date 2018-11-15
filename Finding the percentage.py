dicts = {}
for _ in range(0,int(input())):
    lists = input().split()
    name, scores = lists[0], lists[1:]
    scores = list(map(float,scores))
    dicts[name] = scores

query = input()

qscore=dicts[query]
print(sum(qscore)/(len(list(qscore))))