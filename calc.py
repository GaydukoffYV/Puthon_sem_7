import cmath

def Calc_block(data):
    one_value, oper, tue_value = data
    if oper == '+':
        return sum(one_value, tue_value)
    if oper == '-':
        return sub(one_value, tue_value)
    if oper == '*':
        return mult(one_value, tue_value)
    if (oper =='/') and (tue_value != 0):
        return div(one_value, tue_value)
    else:
        return 'На 0 делить нельзя!'

def sum(one_value, tue_value):
    return one_value + tue_value

def sub(one_value, tue_value):
    return one_value - tue_value

def mult(one_value, tue_value):
    return one_value * tue_value

def div(one_value, tue_value):
    return one_value / tue_value