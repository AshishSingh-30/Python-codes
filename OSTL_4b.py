def prime_no(n):
    
    for i in range(2,101):
        num=i
        flag=0
        for j in range(2,num):
            if num%j==0:
                flag=1
        if flag==0:
            prime.append(num)
    return prime

prime=[]
n=101
prime_no(n)
print(prime)
