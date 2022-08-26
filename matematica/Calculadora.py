from json.encoder import INFINITY
import numpy as np

def soma(va: float, vb: float):
    ''' Função que retorna a soma entre dois valores
    '''
    return va + vb

def sub(va: float, vb: float):
    ''' Função que retorna a subtração entre dois valores
    '''
    return va - vb

def multiplicacao(va: float, vb: float):
    ''' Função que retorna a multiplicação entre dois valores
    '''
    return va * vb

def divisao(va: float, vb: float):
    ''' Função que retorna a divisão entre dois valores
    '''
    if vb == 0:
        return INFINITY
    return va / vb

def media_lista_valores(v:list):
    ''' Função que retorna a média entre N valores
    '''
    if v == [] or v == None:
        return 0

    for i in range(0, len(v)):
        if v[i] == int:
            finalList.append()
            
    return np.mean(v)
