is_even=lambda x: x%2==0
x=int(input("Enter a number:"))
if is_even(x):
    print(f"{x} is even")
else:
    print(f"{x} is odd")