def announce(f):
    # announce função está pegando a função F, e criando uma nova função
    # Podemos chamar de decorator uma função que pega uma função modifica e adicion algumas capacidades e nos da um output
    def wrapper():
        print("About to run a function...")
        
        print("Done with the function.")
        f()
    return wrapper    

# Aqui estamos a pedir para a dicionar a função announce decorator para essa função
@announce
def hello():
    print("Hello, world")    

hello()    