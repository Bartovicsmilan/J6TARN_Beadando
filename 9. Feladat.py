number=600851475143

### Prím szám: 179425889
### Feladat: 600851475143

def IsPrime(n):
    for i in range(n-1,2,-1):
        if n%i==0:
            return False
    return True

def LargestPrime(n):
    primes=[]
    left=n
    j=0
    for i in range(2,n):
        if IsPrime(i)==True:
            primes.append(i)
    p=primes[0]
    while left!=p:
        if left%p==0:
            left=left/p
        elif left%p!=0:
            j+=1
            p=primes[j]
    return p


# print(LargestPrime(number))


def LargestPrimeFactor(numb):
    left=numb
    p=2
    # if IsPrime(numb) is True:
    #     return numb
    while left!=p:
        if left%p==0:#and IsPrime(p)
            left=left/p
            '''print(p)'''
        else:
            p+=1
    return p


print(LargestPrimeFactor(number))