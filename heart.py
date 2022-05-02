Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import *
>>> from random import randrange
>>> from freegames import square, vector
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    from freegames import square, vector
ModuleNotFoundError: No module named 'freegames'
>>> color("red")
>>> begin_fill()
>>> pensize(3)
>>> left(50)
>>> forward(133)
>>> circle(50,200)
>>> right(140)
>>> circle(50,200)
>>> forward(133)
>>> end_fill()
>>> 