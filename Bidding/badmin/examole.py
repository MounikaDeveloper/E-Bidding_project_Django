number=int(input("Enter Number"))

ld=number%10
print("Last digit is",ld)
sum=0
remainder=0

while number>0:
    remainder=number%10
    sum=sum+remainder
    number=number//10
print("first Digit is",remainder)
# print("total sum",sum)
middle=sum-(remainder+ld)
print("Middle Digits Total is",middle)