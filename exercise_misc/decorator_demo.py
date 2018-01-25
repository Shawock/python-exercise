# -*- coding: utf-8 -*-


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print("[warn] %s is running." % func.__name__)
            elif level == "info":
                print("[info] %s is running." % func.__name__)
            elif level == "debug":
                print("[debug] %s is running." % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging("debug")
def foo(text="hello world"):
    print(text)


foo()


class Surround:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print ('class Surround before running')
        self._func(*args, **kwargs)
        print ('class Surround after running')


@Surround
def bar(text="hello"):
    print(text)


bar("fuck surround.")
