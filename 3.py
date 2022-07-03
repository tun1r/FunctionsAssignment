'''Whenever a function is defined inside any other function, the scope of the inner function is defined inside the scope of the outer function.
The outer functions scope is called an enclosing slope.
When a variable is neither local nor global it is an eclosed variable.'''

def hello():
                s1='Hello'
                def world():
                                s2='world'
                                print(s1)
                                print(s2)
                world()
                print(s1)
hello()
