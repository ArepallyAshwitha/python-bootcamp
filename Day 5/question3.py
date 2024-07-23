# input: hello---------wor-----------ld
# output:--------hello world

n=input()
for i in n:
    if(ord(i)==45):
        print("-",end=(" "))
for i in n:
    if(ord(i)==45):
        pass
    else:
        print(i,end=" ")        
