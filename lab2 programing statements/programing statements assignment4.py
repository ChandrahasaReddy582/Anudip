Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
>>> Principal=200
>>> rate=5
>>> time=5
>>> simple_interest=(Principal*rate*time)/100
>>> print(f'The simple Interest on rs.{principal}for{time}years at{rate}% is rs.{simple_interest}')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(f'The simple Interest on rs.{principal}for{time}years at{rate}% is rs.{simple_interest}')
NameError: name 'principal' is not defined. Did you mean: 'Principal'?
>>> print(f'The simple interest on rs.{Principal}for{time}years at{rate}% is rs.{simple_interest}')
The simple interest on rs.200for5years at5% is rs.50.0
