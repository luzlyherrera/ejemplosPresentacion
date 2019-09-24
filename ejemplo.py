# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:17:39 2019

@author: estudiantes
"""

def sumar(lista):
    if not lista:
        return []
    else:
        return lista.pop() + sumar(lista)

def invertir(lista):
    if not lista:
        return []
    else:
        return [lista[-1]] + invertir(lista[0:-1])

def igualarLista(lista1,lista2):
    if len(lista1) != len(lista2):
        return False
    else:
        if not ( lista1 and lista2 ):
            return True
        else: 
            return lista1[0] == lista2[0] and igualarLista(lista1[1::], lista2[1::])

def listaOrdenada(lista):
    if len(lista) <= 1:
        return True
    else:
        return lista[0] < lista[1] and listaOrdenada(lista[1::])

def mostrarUbicacion(lista, pos):
    if not lista:
        return None
    return lista[0] if pos == 0 else mostrarUbicacion(lista[1::], pos-1)

def mayorLista(lista):
    if not lista:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > mayorLista(lista[1::]):
            return lista[0]
        else:
            return mayorLista(lista[1::])

def contarPares(lista):
    if not lista:
        return 0
    elif lista[0] % 2 == 0:
        return 1 + contarPares(lista[1::])
    else:
        return contarPares(lista[1::])

def cuadrados(lista):
    if not lista:
        return []
    else:
        return [lista[0]*lista[0]] + cuadrados(lista[1::])

def divisible(a,b):
    return a % b == 0
def divisibles(x):
    if divisible(x,list(range(1,x))[0]):
        return list(range(1,x))[0]
    else:
        return divisibles(x-1)
def esPrimo(x):
    return len(divisibles(x))<=2
#def primos(x):
    
    
l=list(range(0,10))
l2 = [2,35,65,1,89]
print(divisibles(6))