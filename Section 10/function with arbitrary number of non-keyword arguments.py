# passing as many arguments as we want
def mean(*args):
#    return args # returns a tuple 
    return sum(args) / len(args)

# non-keyword arguments will not work here
print (mean(1,2,3,4))