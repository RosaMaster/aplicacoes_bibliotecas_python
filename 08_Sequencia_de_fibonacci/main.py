### Mostre os primeiros 10 números da sequência de Fibonacci.
### A sequência de Fibonacci é formada pela seguinte fórmula:
### f(n) = f(n-1) + f(n-2)
### Onde f(0) = 0 e f(1) = 1

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

lista = []
for i in range(0, 12):
    
    lista.append(fibonacci(i))
    

print(lista)
