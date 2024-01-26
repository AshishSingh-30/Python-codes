num = int(input("Enter a 3 Digit number: "))
sum = 0
a = num
while a > 0:
    d = a % 10
    sum = sum + d ** 3
    a //= 10
if num == sum:
    print(num , " is an armstrong number")
else:
    print(num , " is not an armstrong number")

