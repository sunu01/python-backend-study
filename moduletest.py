# import mymodule

# mymodule.sayhello()
# print(mymodule.add(4,5))


# from ~ import방식
# from mymodule import sayhello, add
# sayhello()
# print(add(4,5))

from mypackage.greetings import say_hello
from mypackage.math_utils import add
say_hello()
print(add(4,6))