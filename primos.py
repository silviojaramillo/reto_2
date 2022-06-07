#Reto 2
""" 
Calcular los números primos entre dos valores ingresados
por el usuario; en caso de no haber un número primo entre ellos,
buscar el número primo más cercano anterior al primer número 
ingresado y superior al segundo número ingresado por el usuario
"""

#Creando código para intervalo de números primos

start = int(input('Ingrese el mínimo valor del intervalo: '))
end = int(input('Ingrese el máximo valor del intervalo: ')) 

#Arreglo de números primos
prime = []

#Evaluando el número de divisores
def numberDivisors(number):
    divisors = 0
    for i in range(1,(number + 1)):
        if number % i == 0:
            divisors += 1
        else:
            divisors = divisors
    return divisors

#Evaluando la cantidad de números primos
def truePrimes(number1, number2):
    for j in range(number1, (number2 + 1)):
        counter = numberDivisors(j)
        if counter < 3:
            prime.append(j)
    return counter

# Obtener número primo inferior
def primeInferior(condition1, start1):
    while condition1:
        start1 -= 1
        if numberDivisors(start1) == 2:
            prime.append(start1)
            condition1 = False
        


# Obtener número primo superior
def primeSuperior(condition2, end1):
    while condition2:
        end1 += 1
        if numberDivisors(end1) == 2:
            prime.append(end1)
            condition2 = False

#Programa principal
truePrimes(start, end)
if len(prime) == 0:
    primeInferior(True, start)
    primeSuperior(True, end)
    print("El número primo inferior es {} y el número primo superior es {}".format(prime[0], prime[1]))
elif len(prime) == 1:
    print("Los números ingresados son iguales y este, {}, a su vez es un número primo".format(prime[0]))
else:
    print("Los números primos entre {} y {} son: {}".format(start, end, prime))