# create summing function
def add(*args):
    sumofnum = 0
    for eachnum in args:
        sumofnum += eachnum
    return sumofnum 

# production function
def multiply(*arg):
    productofnum = 1
    for eachnum in arg:
        productofnum *= eachnum
    return productofnum

