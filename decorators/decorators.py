#
# def decorator_1(decorated_func):
#     def main_part():
#         print("I am first")
#         decorated_func()
#         print("I am fifth")
#     return main_part
#
#
# def decorator(decorated_func):
#     def main_part():
#         print("I am second")
#         decorated_func()
#         print("I am fourth")
#     return main_part
#
#
# @decorator_1
# @decorator
# def printer():
#     print("i am third")
#
# printer()
#
# def decorator(dec_func):
#     def wrapper(arg1, arg2):
#         print(f"arguments : {arg1}, {arg2}")
#         dec_func(arg1, arg2)
#     return wrapper
#
# @decorator
# def print_arg(arg1, arg2):
#     print(f"{arg1} + {arg2} = {arg1 + arg2}")
#
# print_arg(1, 2)

def decorator(dec_func):
    def wraper(*args, **kwargs):
        s = 0
        for k in args:
            s += k
        print(f"summ of args = {s}")
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")
        dec_func(*args, **kwargs)
    return wraper

@decorator
def test(a,b,c):
    print(a,b,c)
test(1,2,4)