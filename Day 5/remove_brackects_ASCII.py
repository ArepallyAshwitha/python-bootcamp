# remove all the brackects from the given algebric expression.
# 40,41,91,93,123,125

n=input()
for i in n:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end=" ")
print()