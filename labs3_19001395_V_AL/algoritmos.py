import pandas as pd
import re
import numpy as np

#Evaluación REGREX
def evaluate_Fx(str_equ, valX):
  x = valX
  #strOut = str_equ
  strOut = str_equ.replace("x", '*(x)')
  strOut = strOut.replace("^", "**")
  out = eval(strOut)
  print(strOut)
  return out

#Deferencias finitas para derivadas
def evaluate_derivate_fx(str_equ, x, h):
  strOut = str_equ.replace("x", '*(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = "-4*(" + strOut + ")"
  out = eval(strOut)
  
  strOut = str_equ.replace("x", '*(x + 2*h)')
  strOut = strOut.replace("^", "**")
  out = out + eval(strOut)
  
  strOut = str_equ.replace("x", '*(x)')
  strOut = strOut.replace("^", "**")
  strOut = "3*(" + strOut + ")"
  out = out + eval(strOut)
  
  out = -out/(2*h)
  print(out)
  return out

#Resolverdor de Newton
def newtonSolverX(x0, f_x, eps):
  x0 = float(x0)
  eps = float(eps)
  xn = x0
  error = 1
  arrayIters = []
  arrayF_x = []
  arrayf_x = []
  arrayXn = []
  arrayErr = []
  
  i = 0
  h = 0.000001
  while(error > eps):
    print("...")
    x_n1 = xn - (evaluate_Fx(f_x, xn)/evaluate_derivate_fx(f_x, xn, h))
    error = abs(x_n1 - xn)
    i = i + 1
    xn = x_n1
    arrayIters.append(i)
    arrayXn.append(xn)
    arrayErr.append(error)
    solution = [i, xn, error]

  print("Finalizo...")
  TableOut = pandas.DataFrame({'Iter':arrayIters, 'Xn':arrayXn, 'Error': arrayErr})
  return TableOut

def add(a, b):
  a = int(a)
  b = int(b)
  resultado = a + b
  return "El resultado es: " + str(resultado)


# dataset
d = 100
n = 1000
A = np.random.normal(0,1, size=(n,d))
x_true = np.random.normal(0,1, size=(d,1))
b = A.dot(x_true) + np.random.normal(0,0.5,size=(n,1))



def calculate_closed_solution():
    x_star = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)
    # Calcular el valor de la función objetivo f(x*) que es la suma de errores al cuadrado
    f_x_star = np.sum((A.dot(x_star) - b)**2)

    df_x_star = pd.DataFrame(x_star, columns=['x'])
    df_x_star['Valor_de_f(x)'] = f_x_star

    return df_x_star

def rosenbrock(x: np.array):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

def rosenbrock_grad(x):
    grad = np.zeros_like(x)
    grad[0] = -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0])
    grad[1] = 200 * (x[1] - x[0]**2)
    return grad

def rosenbrock_hess(x):
    hess = np.zeros((2, 2))
    hess[0, 0] = 1200 * x[0]**2 - 400 * x[1] + 2
    hess[0, 1] = -400 * x[0]
    hess[1, 0] = -400 * x[0]
    hess[1, 1] = 200
    return hess

def backtracking_line_search(x, p, grad, alpha=0.3, beta=0.8):
    t = 1
    while (rosenbrock(x + t * p) > rosenbrock(x) + alpha * t * np.dot(grad.T, p)):
       t *= beta
    return t

def newton_method(x0, tol=1e-8, max_iter=1000):
    x_k = x0
    iter_count = 0
    results = []
    
    while np.linalg.norm(rosenbrock_grad(x_k)) > tol and iter_count < max_iter:
        grad_k = rosenbrock_grad(x_k)
        hess_k = rosenbrock_hess(x_k)
        p_k = -np.linalg.inv(hess_k).dot(grad_k)
        t = backtracking_line_search(x_k, p_k, grad_k)
        x_k = x_k + t * p_k
        
        # Guardar resultados para la tabla
        results.append([iter_count, x_k, p_k, np.linalg.norm(grad_k)])
        
        iter_count += 1
    
    return results

initial_points = [np.array([0.0, 0.0]), np.array([0.6, 0.6]), np.array([-0.5, 1.0]), np.array([-1.2, 1.0])]

# Ejecutar el método de Newton para cada punto inicial
for x0 in initial_points:
    print(f"\nResultados para el punto inicial {x0}:")
    results = newton_method(x0)
    for r in results:
        print(f"Iteración {r[0]}: x_k = {r[1]}, p_k = {r[2]}, ||grad|| = {r[3]}")