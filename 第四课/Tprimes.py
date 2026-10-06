n=int(input())
l=list(map(int,input().split()))

primes=[True]*1000001
primes[0]=False;primes[1]=False
for i in range(2,1000001):
    if primes[i]:
        for j in range(i*i,1000001,i):
            primes[j]=False
c=set()
for i in range(1000001):
    if primes[i]:
        c.add(i**2)
import math as m
for k in l:
    if k in c:
        print("YES")
    else:
        print("NO")