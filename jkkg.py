import math
p=3
q=7
n=p*q
e=2
phi=(p-1)*(q-1)
while(e<phi):
    if(math.gcd(e,phi)==1):
        break
    else:
        e=e+1
k=2
d=(1+(k*phi))/e
msg=12.0
print("message data=",msg)
c=pow(msg,e)
c=math.fmod(c,n)
print("encrypt data=",c)
m=pow(c,d)
m=math.fmod(m,n)
print("original message sent=",m)   
