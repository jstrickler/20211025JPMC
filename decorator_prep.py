from datetime import datetime
from pprint import pprint
from functools import wraps

all_calls = []

def log_calls(old_function):

    # replacement function
    @wraps(old_function)
    def _(*args, **kwargs):
        all_calls.append((old_function.__name__, datetime.now().ctime()))
        return old_function(*args, **kwargs)

    return _  # return replacement function

@log_calls   # spam = log_calls(spam)
def spam(word):
    print(f"{word} {word} {word}")

@log_calls
def ham():
    print("ham ham ham")
    return 1000

# spam = doit(spam)
# ham = doit(ham)
spam("wombat")  # really calling new_function("wombat")
ham()
spam("hairball")
spam("tractor")
ham()
x = ham()  # really calling _()
print(x)

# result = function(....)

pprint(all_calls)
print()
print(ham, spam)

def foo(word):
    def deco(old_function):
        @wraps(old_function)
        def _(*args, **kwargs):
            print(" ".join([word] * 3))
            return old_function(*args, **kwargs)
        return _
    return deco

@foo("barf")
def thing():
    print("I'm a thing!")

# thing = foo("barf")(thing)
print("name of thing is", thing.__name__)
thing()

@foo("blah")
def moose():
    print("I'm a moose")
moose()


