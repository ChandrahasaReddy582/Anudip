Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 2. Using input function take two number and then swap the number.
>>> a=int(input('Enter the first number:'))
Enter the first number:6
>>> b=int(input('Enter the second number:'))
Enter the second number:5
>>> print(f'Before swapping:a={a},b={b}')
Before swapping:a=6,b=5
>>> a,b=b,a
>>> print(f'After swapping:a={a},b={b}')
After swapping:a=5,b=6
