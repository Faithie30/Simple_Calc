#Make a function that adds two numbers
def add(x,y):
  return x+y

def add(*args):
    sumofnum = 0
    for eachnum in args:
        sumofnum += eachnum
    return sumofnum 

def multiply(x,y):
    return x*y

def multiply(*args):
    productofnum = 1
    for eachnum in args:
        productofnum *= eachnum
    return productofnum

