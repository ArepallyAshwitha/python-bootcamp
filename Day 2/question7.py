my_list=list(map(int,input().split()))
sum=0
n=len(my_list)
a=n/2
avg=0
for i in range(0,len(my_list),2):
        sum+=my_list[i]
avg=sum//a
print(avg)
