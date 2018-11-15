n = int(input())
marksheet = []
for _ in range(0,n):
    marksheet.append([input(),float(input())])

sechigh=sorted(list(set(marks for name, marks in marksheet)))[1]

print("\n".join([a for a,b in sorted(marksheet) if b == sechigh]))