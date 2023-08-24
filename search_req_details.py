a=open('request_details.txt','r')
c=a.read()
m=c.find("input type=")                print(m)
e=str(c)
x=m+20
g=e[m:x]
print(g)
