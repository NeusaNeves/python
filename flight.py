class Flight():
    # A função init cria um novo voo
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # add_passenger adiciona novos passageiros no avião
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)    
        return True

    #open_seats nos diz quantos lugares vazios tem no avião
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

# Temos uma lista de pessoas e para cada uma dessas pessoas vammos tentar asicionar ela no avião 
people = ["Harry", "Hermione", "Ginny"]
for person in people: 
    if flight.add_passenger(person):
        print(f"Adicionado {person} no avião com sucesso.")
    else:
        print(f"Não tem lugares disponíveis para {person}")    