# input:ABC,4
# output:EFG

n=input()
s=int(input())
for i in n:
        if(ord(i)>=65 and ord(i)<=90):
            print(chr(ord(i)+s),end=" ")