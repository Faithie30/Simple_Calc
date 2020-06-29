# create summing function
def add(*args):
    sumofnum = 0
    for eachnum in args:
        sumofnum += eachnum
    return sumofnum 

# production function
def multiply(*args):
    productofnum = 1
    for eachnum in args:
        productofnum *= eachnum
    return productofnum

