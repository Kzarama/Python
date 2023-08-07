from decorators.decorators import func_test, repeat, timer, debug


@func_test
def hi(name: str):
    """documentation for the hi function"""
    return f"hi {name}"


# help(hi)
print(hi("kevin"))


@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


greet("World")


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(1)


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting("Benjamin")

make_greeting("Richard", age=112)
