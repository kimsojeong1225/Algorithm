N=int(input())
plans = input().split()
x,y =1,1

for_x=[-1,1,0,0]
for_y=[0,0,1,-1]
z=['U','D','R','L']

for i in plans :
  for j in range(len(z)):
    if i == z[j]:
      nx = x + for_x[j]
      ny = y + for_y[j]

      if nx<1 or nx>N:
        nx=x
      elif ny<1 or ny>N:
        ny=y
    else : continue
  
  x=nx
  y=ny

print(x,' ',y)
