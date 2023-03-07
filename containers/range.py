def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    HINT:
    If you can figure out how to use the built-in range f
    unction (without modifying the test cases!),
    then feel free to do so.
    That's fairly difficult to do, however, and it's m
    uch easier to just implement this fun
    ction normally using the yield syntax.

    NOTE:
    For efficiency reasons, Python's built-in range ob
    ject is written in the C programming langua
    ge rather than natively in python.
    You can find the source code online a
    t https://hg.python.org/cpython/f
    ile/ee7b713fec71/Objects/rangeobject.c
    The link takes you to a file that is 1445 lines long,
    and all it does is implement t
    his simple functionality.
    My easy to read Python implementation of t
    his function is just 15 lines long.
    (And with some code golf I also wrote a l
    ess readable version that is only 4 lines.)
    It is very common for C programs to be 100x lon
    ger than their corresonding python programs.
    C code must manage lots of details about the c
    omputer manually that python code automates for you.
    Carefully written C code can be faster than the co
    rresponding python code because it can remo
    ve some of the overhead of this automation process,
    but the resulting code is much longer and harder to read/write.
    '''

    i = -1
    if b is None and c is None:
        while i < (a - 1):
            i += 1
            yield i
    if b is not None and c is None:
        i = (a - 1)
        while i < (b - 1):
            i += 1
            yield i
    if b is not None and c is not None:
        if a < b and c < 0:
            return []
        if a > b and c > 0:
            return []
        if b > 0:
            i = (a - c)
            while (b - i) > 0:
                i += c
                if i <= (b - 1):
                    yield i
        if b < 0:
            i = (a - c)
            while (b - i) < 0:
                i += c
                if i >= (b + 1):
                    yield i
