#!/usr/bin/python
#
#
import os
str = input("Enter your input: ")
print ("Received input is : ", str)

fo = open("globalvariable.py", "a+")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.write("Python is a great language.\nYeah its great!!\n")
fo = open("globalvariable.py", "a+")
position = fo.tell()
print ("Current file position : ", position)
str = fo.read()
position = fo.seek(0, 0)
print ("Read String is : ", str)
fo.close()
print ("Closed or not : ", fo.closed)
os.rename( "globalvariable.py", "globalvariablenew.py" )
