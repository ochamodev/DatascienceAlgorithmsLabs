import pandas as pd
import sympy as sym
import re

def processEquation(equation):
    strOut = equation.replace('^', '**')
    x = sym.symbols('x')
    expr = sym.sympify(strOut)
    print(expr)
    def f(value):
      return float(expr.subs(x, value))

    return f


def bisectionMethod(equation, interval, tol, maxIter):
    try:
        f = processEquation(equation)
        intervalItems = interval.split(',')
        print(intervalItems)
        a = float(intervalItems[0])
        b = float(intervalItems[1])
        tol = float(tol)
        maxIter = int(maxIter)
        results = []
    except ValueError as e:
        print(e)
    for k in range(maxIter):
        c = (a + b) / 2
        fc = f(c)
        error = (abs(a - b) / 2)
        results.append({
            'iteration': k + 1,
            'x_k': fc,
            'punto medio': c,
            'a': a,
            'b': b,
            'Error': error
        })
        if (abs(fc) < tol):
            break
        elif (f(a) * fc < 0):
            b = c
        else:
            a = c

    bisectionOutput = pd.DataFrame(results)

    return bisectionOutput
    
