# Crear um set vazio
s = set()

# Adicionar elementos no set, ele não adiciona duas vezes o mesmo elementos
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

# Para remover um elemento 
s.remove(2)
print(s)

#  Calcular quantos elementos a gente tem dentro do S., É só usar o LEN(Nome da var)
print(f"O set tem {len(s)} elementos.")