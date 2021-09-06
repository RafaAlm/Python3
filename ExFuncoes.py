# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números

def imprimeSec():
  for i in range(2,20,2):
    print(i)

imprimeSec()

# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def imprimiStr():
  frase = str(input("Digite sua frase:"))

  return frase.upper()

imprimiStr()

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def imprimiList(lista):
  lista.append(5)
  lista.append(6)

lista1 = [1,2,3,4]

imprimiList(lista1)

print(lista1)

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
# o simbolo '*' indica que o parametro podera receber varios valores

def multChamada(num, *lista):
    print(num)

    for i in lista:
      print(i)  

multChamada('a','b','c')
multChamada(25)

# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles

soma = lambda arg1,arg2: arg1+arg2

print("A soma é :", soma(15,15))

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)

# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print (list(Fahrenheit))

# Exercício 8
# Crie uma lista e liste todos os métodos e atributos da lista

lista = ()

dir(lista)

# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.

import pandas as pd

dir(pd)

# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
import pandas as pd
file_name = "binary.csv"

def retornaArq(file_name):
    df = pd.read_csv(file_name)
    return df.describe()
    
retornaArq(file_name)