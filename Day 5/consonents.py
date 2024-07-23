# write a program to print all the consonents in a given string

vowel="aeiou"
consonent="bcdnghjklmnpqrstvwxyz"
count=0
c=0
i="hello wOrld"
str=i.lower()
for i in str:
    if (i in vowel):
        count+=1 
for i in str:
    if (i in consonent):
        c+=1 
print(count,c)        