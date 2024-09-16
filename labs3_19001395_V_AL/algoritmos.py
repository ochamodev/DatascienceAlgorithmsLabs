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

def compute_cost(A, b, x):
    return np.mean((A.dot(x) - b) ** 2)

def gradient_descent(lr=0.001, num_iter=1000):
    n, d = A.shape
    x = np.zeros((d, 1))
    for i in range(num_iter):
        gradient = 2 * A.T.dot(A.dot(x) - b) / n
        x -= lr * gradient
    
    f_x_star = compute_cost(A, b, x)

    df_x_star = pd.DataFrame(x, columns=['x'])
    df_x_star['Valor_de_f(x)'] = f_x_star
    return df_x_star

def stochastic_gradient_descent(lr=0.001, num_iter=1000):
    n, d = A.shape
    x = np.zeros((d, 1))
    for i in range(num_iter):
        idx = np.random.randint(n)
        A_i = A[idx:idx+1]
        b_i = b[idx:idx+1]
        gradient = 2 * A_i.T.dot(A_i.dot(x) - b_i)
        x -= lr * gradient

    f_x_star = compute_cost(A, b, x)

    df_x_star = pd.DataFrame(x, columns=['x'])
    df_x_star['Valor_de_f(x)'] = f_x_star
    return df_x_star

def mini_batch_gradient_descent(lr=0.001, batch_size=32, num_iter=1000):
    n, d = A.shape
    x = np.zeros((d, 1))
    for i in range(num_iter):
        idx = np.random.choice(n, batch_size, replace=False)
        A_batch = A[idx]
        b_batch = b[idx]
        gradient = 2 * A_batch.T.dot(A_batch.dot(x) - b_batch) / batch_size
        x -= lr * gradient
        
    f_x_star = compute_cost(A, b, x)

    df_x_star = pd.DataFrame(x, columns=['x'])
    df_x_star['Valor_de_f(x)'] = f_x_star
    return df_x_star

def backtracking_line_search_gd(A, b, x, alpha=0.3, beta=0.8):
    # Calculate the initial gradient
    gradient = 2 * A.T.dot(A.dot(x) - b) / A.shape[0]
    
    # Initial step size
    step_size = 1.0
    
    # Calculate the initial cost
    cost = np.mean((A.dot(x) - b) ** 2)
    
    while True:
        # Update x with the current step size
        x_new = x - step_size * gradient
        
        # Calculate the new cost
        new_cost = np.mean((A.dot(x_new) - b) ** 2)
        
        # Check the Armijo condition
        if new_cost <= cost - alpha * step_size * np.linalg.norm(gradient) ** 2:
            break
        
        # Reduce step size
        step_size *= beta
    
    return step_size

def convert_input_to_numpy(input_text):
    # Elimina espacios en blanco y separa por comas
    str_values = input_text.strip().split(',')
    
    # Convierte las cadenas en números flotantes
    float_values = [float(val) for val in str_values]
    
    # Convierte la lista a un array NumPy con forma (d, 1)
    np_array = np.array(float_values).reshape(-1, 1)
    
    return np_array

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

# Método de Gradient Descent con Backtracking Line Search
def gradient_descent_backtracking(x_init, tol=1e-6, max_iter=1000):
    x = convert_input_to_numpy(x_init)
    for i in range(max_iter):
        grad = rosenbrock_grad(x)  # Calcular el gradiente en el punto actual
        direction = -grad  # Dirección de descenso (negativo del gradiente)
        
        # Aplicar Backtracking Line Search para obtener el mejor tamaño de paso
        alpha = backtracking_line_search(x, direction, grad)
        
        # Actualizar x usando el tamaño de paso obtenido
        x_new = x + alpha * direction
        
        # Verificar la convergencia
        if np.linalg.norm(x_new - x) < tol:
            print(f"Convergió después de {i} iteraciones.")
            break
        
        x = x_new
    
    return x

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

def newton_method_backtrack(x_0: str, step_size: str):
    x_0 = x_0.split(",")
    x_0[0], x_0[1] = float(x_0[0]), float(x_0[1])
    step_size = int(step_size)

    output = newton_method(x_0, step_size)

    return output
