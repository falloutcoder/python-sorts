import timeit
from collections import namedtuple

def _template_func(setup, func):
    """
    Monkey Patching original timer function's _template_func.
    This is used if the "statement" is a callable. and returns a
    namedtuple containing 'output' property which has callable's
    result and 'time' property which has time taken by the  to complete
    """

    Result = namedtuple('Result', ['time', 'output'])
    def inner(_it, _timer, _func=func):
        setup()
        _t0 = _timer()
        for _i in _it:
            output = _func()
        _t1 = _timer()
        timetaken = _t1 - _t0
        return Result(timetaken, output)
    return inner

timeit._template_func = _template_func

def timethis(fun):
    def _wrapped(*args, **kwargs):
        t = timeit.Timer(lambda: fun(*args, **kwargs))
        return t.timeit(number=kwargs.pop('repeat', 1))
    return _wrapped
