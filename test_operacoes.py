import pytest
from matematica.Calculadora import *

def test_soma():
    v1 = 1.0
    v2 = 4.0
    assert 5 == soma(v1,v2)

def test_multiplicacao():
    v1 = 0.0
    v2 = 7.0
    assert 0 == multiplicacao(v1,v2)

def test_multiplicacao2():
    v1 = 10.0
    v2 = 7.0
    assert 70 == multiplicacao(v1,v2)