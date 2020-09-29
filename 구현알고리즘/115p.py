x = input()
count=0
cols = ['','a','b','c','d','e','f','g','h']
col = cols.index(x[0])
row = int(x[1])

case1 =[2,1]
case2=[2,-1]
case3=[1,2]
case4=[-1,2]
case5=[-2,1]
case6=[-2,-1]
case7=[1,-2]
case8=[-1,-2]


case1[0]+=col
case1[1]+=row
if case1[0]<=8 and case1[1]<=8 and case1[0]>0 and case1[1]>0:
  count+=1
case2[0]+=col
case2[1]+=row
if case2[0]<=8 and case2[1]<=8 and case2[0]>0 and case2[1]>0:
  count+=1
case3[0]+=col
case3[1]+=row
if case3[0]<=8 and case3[1]<=8 and case3[0]>0 and case3[1]>0:
  count+=1
case4[0]+=col
case4[1]+=row
if case4[0]<=8 and case4[1]<=8 and case4[0]>0 and case4[1]>0:
  count+=1
case5[0]+=col
case5[1]+=row
if case5[0]<=8 and case5[1]<=8 and case5[0]>0 and case5[1]>0:
  count+=1
case6[0]+=col
case6[1]+=row
if case6[0]<=8 and case6[1]<=8 and case6[0]>0 and case6[1]>0:
  count+=1
case7[0]+=col
case7[1]+=row
if case7[0]<=8 and case7[1]<=8 and case7[0]>0 and case7[1]>0:
  count+=1
case8[0]+=col
case8[1]+=row
if case8[0]<=8 and case8[1]<=8 and case8[0]>0 and case8[1]>0:
  count+=1


print(count)





input_data = input()
count=0
row = int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1

steps=[(-2,-1),(-2,1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]

for step in steps :
  next_row=row+step[1]
  next_col=column+step[0]

  if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
    count+=1

print(count)
