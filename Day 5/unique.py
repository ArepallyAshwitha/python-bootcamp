# print the non repeating characters in a given string
                   #or#
# print the unique characters in a given string

vowels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
ans=" "
i="hello wOrld"
inp=i.lower()
for i in inp:
    if (i not in ans):
        ans+=i
print(ans)                