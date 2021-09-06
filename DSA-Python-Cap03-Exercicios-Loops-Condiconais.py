#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 3</font>
# 
# ## Download: http://github.com/dsacademybr

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios - Loops e Condiconais

# In[ ]:


# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"


# In[ ]:



for i in range(1,8):
    resposta = input("qual o dia da semana?\n")
    
    if((resposta == 'sabado') or (resposta == 'domingo' )):
        print("\nHoje é dia de descanso\n")
    else:
        print("\nHoje é dia de trabalhar\n")


# In[ ]:


# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista


# In[ ]:


frutas = ['laranja','morango','goiaba','jabuticaba','banana']

for i in frutas:
    if(i == 'morango'):
        print("Morango encontrado")
        


# In[ ]:


# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista


# In[ ]:


tupla = (1,2,3)
lista = []

for i in tupla:
    mult = i *2
    
    lista.append(mult) 

print(lista)


# In[ ]:


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela


# In[ ]:


for i in range(100,152,2):
    print(i)


# In[ ]:


# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela


# In[4]:


temperatura = 40
count = 0
while(temperatura > 35):
    print(temperatura)
    temperatura -=1
    


# In[ ]:


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa


# In[5]:


contador = 0

while(contador <100):
    if(contador == 23):
        break
    print(contador)
    contador +=1
    


# In[ ]:


# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista


# In[17]:


numeros = list()
valor = 4

while(valor <= 20):
    numeros.append(valor)  
    valor = valor + 2

print(numeros) 


# In[18]:


# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = range(5, 45, 2)


# In[21]:


print(list(nums))


# In[23]:


# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')


# In[27]:


# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."

contador = 0

for caracter in frase:
    if caracter == 'r':
        contador+=1
print("O caracter r aparece %s na frase." %(contador))       


# # Fim

# ### Obrigado
# 
# ### Visite o Blog da Data Science Academy - <a href="http://blog.dsacademy.com.br">Blog DSA</a>
