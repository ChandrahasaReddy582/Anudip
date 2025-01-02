Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
>>> num=int(input('Enter a number:'))
Enter a number:5
>>> print('Even' if num%2==0 else 'odd')
odd
>>> num=int(input('Enter a number:'))
Enter a number:6
>>> print('Even' if num%2==0 else 'odd')
Even
