n,m,k = map(int,input().split())
data=list(map(int,input().split()))

data.sort()
sum = 0

sum = data[-1] * k * int(m/(k+1)) + data[-1]*int(m%(k+1))
sum += data[-2]*int(m/(k+1))

print(sum)
