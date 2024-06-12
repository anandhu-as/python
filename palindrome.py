num = int(input("Enter a number: "))
rev = 0
x=num
if num > 0:
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10

print("reverse of number is " , rev)

if x==rev: 
    print(f"{x} is palindrome")
else:
    print(f"{x} is not palindrome")
    
