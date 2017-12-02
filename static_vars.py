"""
Python has a number of hacky ways to use static variables a la C/C++:

int count(){
  static int counter = 0;
  return ++counter;
}

This simple example might be well translated by using a generator, but for other
uses of static variables, we can add attributes to a function.  Since Python
treats functions as objects, and in any given context they will be unique,
then we can assign and access attributes of the function in every call.

Note that there is nothing preventing them from being changed, there is no
real mechanism for private variables in Python.  That said, we still get the benefit
of a single assignment for commonly used variables in a function.

Thanks to user Claudiu on StackExchange for this idea
https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function#279586

"""

# The decorator gives an elegant way to associate variables with a function
def addStatics(**kwargs):
    def amendFunc(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return amendFunc

# Here, we add three variables
@addStatics(_a=1,_b=2,_c=3)
def foo():
    print("Called foo")
    print("a: {}\nb: {}\nc: {}\n".format(foo._a, foo._b, foo._c))

if __name__ == "__main__":
    # Note: Across calls, the attribute values are preserved
    foo()
    foo()
    
    # Note: The attributes can still be changed.  Here, we use the
    # class convention for naming of variables intended to be private
    # to discourage changing them
    foo._a = foo._b = foo._c = 0
    foo()
    foo()
