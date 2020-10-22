#What are Functions?
#=a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable...
#what's a block in python??
#block_head: 
    #1st block line
    #2nd block line

#note:block_head:<=>block_keyword block_name(argument1,argument2, ...)
#unctions in python are defined using the block keyword "def"
def function1():
    print("my first function")

#Functions may also receive arguments
def function2(x):
    print("Hello %s to my second function" %x)

#Functions may return a value to the caller, using the keyword- 'return' 
def sum_function(a,b):
    return a+b

#How do you call functions in Python??
  #call function1
function1()
  #call function2
function2("network")
  #call sum_function
sum=sum_function(5,3)
print("sum = %d" %sum)
