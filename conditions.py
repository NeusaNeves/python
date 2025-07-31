# n = input("Number: ")

# if n > 0:
#     print("n é positivo")
# elif n < 0:
#     print("n é negativo")  
# else:
#     print("n não é positivo")

# TypeError: '>' not supported between instances of 'str' and 'int' Esse é um erro, quando o ele está a espera de um tipo, mas acaba sendo um outro

n = int(input("Number: "))

if n > 0:
    print("n é positivo")
elif n < 0:
    print("n é negativo")  
else:
    print("n não é positivo")