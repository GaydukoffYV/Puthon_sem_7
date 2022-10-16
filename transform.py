import view as c_ui
from fractions import Fraction
import cmath
from calc import Calc_block as c_calc
import transform as d_t


def data_formatting(data):
    data_type, one_value, oper, tue_value = data

    if data_type == '1':

        one_value = complex(one_value)

        tue_value = complex(tue_value)

    elif data_type == '2':

        a = one_value
        one_value = Fraction(int(a[0: a.index(
            '/')]), int(a[a.index('/')+1:len(a)]))

        g = tue_value
        tue_value = Fraction(int(g[0: g.index(
            '/')]), int(g[g.index('/')+1:len(g)]))

    return (one_value, oper, tue_value)