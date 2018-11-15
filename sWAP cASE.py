s = input()
print("".join([i.lower() if i.isupper() else i.upper() for i in s]))
print(s.swapcase())