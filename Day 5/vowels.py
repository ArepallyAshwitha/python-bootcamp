# check how many mobiles are in a given string

str=input()
check=['a','e','i','o','u']
count=0
for i in str:
    if (i in check):
        count+=1
print(count)         