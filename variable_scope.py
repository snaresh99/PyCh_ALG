# Python example to demonstrate variable scope
a=10; b=20
def my function():
  global a
  a = 11; b=21
my_function()
print(a) => 11
print(b) => 20
RPI4_NIDAQ6002.ipynb