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
# bar3()


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
# 下面的装饰器等价于：
#   wrap_html(tag_name="b", css_class="outer")(wrap_html(tag_name="i", css_class="inner")(bar4))()
@wrap_html(tag_name="b", css_class="outer")
@wrap_html(tag_name="i", css_class="inner")
def bar4():
    # expect result: <b class="outer"><i class="inner">hello world</i></b>
    return "hello world"


# print(bar4())


def make_html_tag(tag, *args, **kwargs):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwargs["css_class"]) \
            if "css_class" in kwargs else ""

        def wrapped():
            return "<" + tag + css_class + ">" + fn() + "</" + tag + ">"

        return wrapped

    return real_decorator


@make_html_tag(tag="b", css_class="bold_css")
@make_html_tag(tag="i", css_class="italic_css")
def bar5():
    return "hello world"


# print(bar5())


class ClassDecorator:
    """
    当无参装饰器时，待装饰的函数通过 __init__ 传入
    __call__ 充当了装饰后的函数
    """

    def __init__(self, fn):
        # print("ClassDecorator init, fn = %s" % fn.__name__)
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print('fn before execute %s' % self.fn.__name__)
        self.fn()


# 解释器遇到类装饰器时就会进行初始化
@ClassDecorator
def bar6():
    print('hello bar6')


# print('bar6 execute after')

# bar6()


class MakeHtml:
    """
    当有参装饰器时，参数通过 __init__ 传入
    __call__ 需要返回装饰函数
    """

    def __init__(self, tag, **kwargs):
        self._tag = tag
        self._css_class = " class='%s'" % kwargs["css_class"] if "css_class" in kwargs else ""

    def __call__(self, fn):
        def wrapper():
            # return "<" + self._tag + self._css_class + ">" + fn() + "</" + self._tag + ">"
            return "<%s%s>%s</%s>" % (self._tag, self._css_class, fn(), self._tag)

        return wrapper


@MakeHtml(tag="body", css_class="global")
@MakeHtml(tag="div", css_class="outer")
@MakeHtml(tag="span", css_class="inner")
def bar7():
    return "hello world"


# print(bar7())


def decorate_param(fn):
    # 被装饰函数的参数会被注入到 wrapper 中
    def wrapper(*args, **kwargs):
        kwargs["key1"] = "value1"
        fn(*args, **kwargs)

    return wrapper


@decorate_param
def bar8(*args, **kwargs):
    print(kwargs["key1"])


# bar8()


def user_interceptor(fn):
    def wrapper(*args, **kwargs):
        import random
        user_id = random.randint(10, 50)
        kwargs["key1"] = "value " + str(random.randint(1, 100))
        fn(user_id, *args, **kwargs)

    return wrapper


@user_interceptor
def bar9(user_id, *args, **kwargs):
    print("user_id = %s, key1 = %s" % (user_id, kwargs["key1"]))


# bar9()


def decorator10(fn):
    from functools import wraps

    @wraps(fn)
    def wrapper():
        """ this is wrapper doc """
        print("before fn %s" % fn.__name__)
        fn()
        print("after fn %s" % fn.__name__)

    return wrapper


@decorator10
def bar10():
    """ this is bar10 doc """
    print("hello bar10")


bar10()
print("bar10 info: [%s, %s, %s]" % (bar10.__name__, bar10.__doc__, bar10.__module__))
