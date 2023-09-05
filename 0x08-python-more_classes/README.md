0x08-python-more_classes

0-rectangle.py
	.Write an empty class rectangle that defines  rectangle
	
    You are not allowed to import any module

guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$ 

1-rectangle.py
	.Write a class rectangle that defines a rectangle by: (based on 0-rectangle.py
