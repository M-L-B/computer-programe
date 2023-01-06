list=[]
n=1
m1,m2,m3,m4=0,0,0,1
while n!=0:
    list.append(n)
    n=int(input())
    list_len=len(list)
for x in range (1,list_len,1):
  y=list[x]
  for z in range(y-1):
      m4=m4+m3
      m3=m2
      m2=m1
      m1=m4
  print(m1+m2+m3+m4)
  m1,m2,m3,m4=0,0,0,1