#!/usr/bin/python

#####################################
# module: antideriv.py
# Krista Gurney
# A01671888
#####################################

from const import const
from pwr import pwr
from var import var
from plus import plus
from prod import prod
from quot import quot
from maker import make_const, make_pwr, make_prod, make_plus, make_ln, make_absv
import math

def is_e_const(b):
    return b.get_val() == math.e

def antideriv(i):
    ## CASE 1: i is a constant
    if isinstance(i, const):
        #3 => 3x^1
        return prod(i, make_pwr('x', 1.0))
    ## CASE 2: i is a pwr
    elif isinstance(i, pwr):
        #x^d => 1/(d+1) * x^(d+1)
        b = i.get_base()
        d = i.get_deg()
        ## CASE 2.1: b is var and d is constant.
        if isinstance(b, var) and isinstance(d, const):
            if d.get_val() == -1:
                return make_ln(make_absv(pwr(b, const(1.0))))
            else:
                r = const(d.get_val() + 1.0)
                return prod(quot(const(1.0), r), pwr(b, r))
        ## CASE 2.2: b is e
        elif is_e_const(b):# e^(kx) => 1/k  * e(kx)
            if isinstance(d, prod):
                k = d.get_mult1()
                return prod(quot(const(1.0), k), i)
            else:
                raise Exception('antideriv: unknown case')
        # ## CASE 2.3: b is a sum
        elif isinstance(b, plus):#(1+x)^-3
            r = const(d.get_val()+1.0)
            return prod(quot(const(1.0), r), pwr(b, r))
        else:
            raise Exception('antideriv: unknown case')
    ### CASE 3: i is a sum, i.e., a plus object.
    elif isinstance(i, plus):
        ## your code here
        pass
    ### CASE 4: is is a product, i.e., prod object,
    ### where the 1st element is a constant.
    elif isinstance(i, prod):
        ## your code here
        pass
    else:
        raise Exception('antideriv: unknown case')

                     
            
    
    
