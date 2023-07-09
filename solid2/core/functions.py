from decimal import Decimal
from solid2 import scad_inline as i
from solid2.core.object_base.object_base_impl import OpenSCADConstant

def _encode(var):
    if type(var) in (list, tuple):
        return ''.join([
            '[',
            ', '.join([
                _encode(item)
                for item in var
            ]),
            ']',
        ])
    elif type(var) in (int, float, Decimal, OpenSCADConstant):
        return str(var)
    elif type(var) is str:
        return f'"{var}"'
    else:
        raise Exception(f"Can't handle variable type {type(var)} for {var}")

def _convert(array):
    return _encode(array)[1:-1]

def _convert_vector(v):
    return _encode(v)

def cos(n):
    return i(f'cos({n})')

def sin(n):
    return i(f'sin({n})')

def tan(n):
    return i(f'tan({n})')

def acos(n):
    return i(f'acos({n})')

def asin(n):
    return i(f'asin({n})')

def atan(n):
    return i(f'atan({n})')

def atan2(n, m):
    return i(f'atan2({n}, {m})')

def abs_(n):
    return i(f'abs({n})')

def ceil(n):
    return i(f'ceil({n})')

def concat(*args):
    parameters = _convert(args)
    return i(f'concat({parameters})')

def cross(*args):
    parameters = _convert(args)
    return i(f'cross({parameters})')

def exp(n):
    return i(f'exp({n})')

def floor(n):
    return i(f'floor({n})')

def ln(n):
    return i(f'ln({n})')

#
def len_(n):

    return i(f'len({n})')

def log(n):
    return i(f'log({n})')

def lookup(*args):
    parameters = _convert(args)
    return i(f'lookup({parameters})')

def max_(*args):
    parameters = _convert(args)
    return i(f'max({parameters})')

def min_(*args):
    v = _convert_vector(args)
    return i(f'min({v})')

def norm(v):
    v = _convert_vector(v)
    return i(f'norm({v})')

def pow_(n, m):
    return i(f'pow({n}, {m})')

def rands(*args):
    parameters = _convert(args)
    return i(f'rands({parameters})')

def round_(n):
    return i(f'round({n})')

def sign(n):
    return i(f'sign({n})')

def sqrt(n):
    return i(f'sqrt({n})')
