x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

y = "awesome"

def myfunc():
  print("Python is " + y)

myfunc()

global z
z=7
def myglobal():
   print(z)

myglobal()
