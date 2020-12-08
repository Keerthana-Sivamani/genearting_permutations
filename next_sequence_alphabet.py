s=input().strip()
p=0
for i in range(len(s)):
    if list(s[i:])==sorted(s[i:])[::-1]:
        p=i
        break
for i in range(len(s)-1,p-1,-1):
    if s[i]>s[p-1]:
        b=s[i];l=i
        break
d=str(s[p-1])+str(s[p:i])+str(s[i+1:])
g=''
for i in sorted(d):
    g+=i
print(s[:p-1]+b+g)