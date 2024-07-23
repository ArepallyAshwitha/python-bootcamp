# print all the vowels followed by consonents

vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
ans=" "
i="hello wOrld"
inp=i.lower()
for i in inp:
    if i in vowels:
        ans+=i
for i in inp:
    if i in consonents:
        ans+=i
print(ans)                

    