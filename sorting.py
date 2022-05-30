student@student-ThinkPad-X250:~$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> zuch=["asd","pd","d"]
>>> for word in zuch:print(len(word))
... 
3
2
1
>>> #arrange index according to number hierachy.
>>> #create list and loop through each item
>>> #sort the length
>>> #create a variable holding the sorted length of z
>>> #assign the variable to z 
>>> zuch=["asd","pd","d"]
>>> for word in zuch:print(sorted(len(word)))
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> for word in zuch:print(sorted(len(zuch)))
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> zuch.count()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: count() takes exactly one argument (0 given)
>>> count(zuch)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count' is not defined
>>> #len exactly gives one argument,we cannot sort an integer
>>> for word in zuch:print(len(word[0]))
... 
1
1
1
>>> for word in zuch:print(len(word[9]))
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> for word in zuch:print(len(word[1]))
... 
1
1
Traceback (most recent call last):

