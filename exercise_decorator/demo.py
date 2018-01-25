# -*- coding: utf-8 -*-


def foo(fn):
    def wrapper():
        print("fn before execute %s" % fn.__name__)
        fn()
        print("fn after execute %s" % fn.__name__)

    return wrapper


@foo
def bar():
    print("hello bar")


# bar()

# foo(bar)()


def decorator_one(fn):
    def wrapper():
        print("decorator_one execute %s" % fn.__name__)
        fn()

    return wrapper


def decorator_two(fn):
    def wrapper():
        print("decorator_two execute %s" % fn.__name__)
        fn()

    return wrapper


@decorator_one
@decorator_two
def bar2():
    print("hello bar2")


# bar2()


def decorator_three(arg1, arg2):
    def real_decorator(fn):
        def wrapper():
            print("fn before execute, %s, %s, %s" % (arg1, arg2, fn.__name__))
            fn()

        return wrapper

    return real_decorator


@decorator_three("three_one", "three_two")
def bar3():
    print("hello bar3")


# bar3() == decorator_three("three_one", "three_two")(bar3)()
bar3()


def wrap_html(tag_name, *args, **kwargs):
    def real_decorator(fn):
        def wrapper():
            origin_content = fn()
            if "css_class" in kwargs:
                return "<%s class=\"%s\">%s</%s>" % (tag_name, kwargs["css_class"], origin_content, tag_name)
            else:
                return "<%s>%s</%s>" % (tag_name, origin_content, tag_name)

        return wrapper

    return real_decorator


# 普通函数和普通变量命名用小写字母，单词之间用 _ 分割
# wrap_html(tag_name="b", css_class="outer")(wrap_html(tag_name="i", css_class="inner"))()
# @wrap_html(tag_name="b", css_class="outer")
# @wrap_html(tag_name="i", css_class="inner")
def bar4():
    # <b class="outer"><i class="inner">hello world</i></b>
    return "hello world"


# print(bar4())

print(wrap_html(tag_name="b", css_class="outer")(wrap_html(tag_name="i", css_class="inner")(bar4))())
