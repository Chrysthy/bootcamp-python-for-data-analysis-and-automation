# covertendo uma variável float para um número inteiro
print(int(1.0)) # 1
print(int(1.9)) # 1
print(int(1.97226982254)) # 1

# passando para o construtor um valor com string, desde que seja um número válido
print(int("10")) # 10

# covertendo uma string pra float
print(float("10.10"))

# convertendo um numero inteiro para float
print(float(100))

# convertendo para uma string e usando o type para saber qual o tipo de variável
# print((str(10.10))

print(type(str(10.10)))


valor = 10
valor_str = str(valor)

print(type(valor)) # <class 'int'>
print(type(valor_str)) # < class 'string'>

print(100 / 2) # 50.0 (dá um float)
print(100 // 2) # 50 (retorna a parte inteira, um int)