"""

This demonstrates the use of object properties as a way to give the illusion of private members and
getters/setters per object oriented programming. Variables prefixed by underscore are a signal to other
programmers that they should be changing them directly, but there really isn't any enforcement. There are
still ways around it, but this makes it harder to change members that shouldn't change.

"""

class myThing(object):
  def __init__(self, foo=None):
    self._foo = foo

  # This decorator acts as a getter, accessed with "myFoo.foo"
  @property
  def foo(self):
    return self._foo

  # This decorator acts as a setter, but only once
  @foo.setter
  def foo(self, newFoo):
    if self._foo is None:
      self._foo = newFoo
    else:
      raise Exception("Immutable member foo has already been assigned...")

  # This decorator protects against inadvertent deletion via "del myFoo.foo"
  @foo.deleter
  def foo(self):
    raise Exception("Cannot remove immutable member foo")



if __name__ == "__main__":
  myFoo = myThing()
  print(myFoo.foo)
  myFoo.foo = "bar"
  print(myFoo.foo)
  try:
    myFoo.foo = "baz"
  except Exception as e:
    print(e)
  print(myFoo.foo)
  try:
    del myFoo.foo
  except Exception as e:
    print(e)
