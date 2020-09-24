n,m = map(int,input().split())

min_value=[]
for i in range(n):
  i=min(list(map(int,input().split())))
  min_value.append(i)

result = max(min_value)

print(result)
