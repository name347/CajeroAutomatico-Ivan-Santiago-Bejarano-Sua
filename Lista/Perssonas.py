ListaPersonas = []

Persona = {"Nombre": "Ivan", "Edad": 20, "Ciudad": "San Martin"}

ListaPersonas.append(Persona)

Persona["Edad"] = 21    

Persona["Profesion"] = "Programador"

del Persona["Ciudad"]

email = Persona.get("Email", "No se ha proporcionado un email") 

for clave, valor in Persona.items():
    print(f"{clave}: {valor}") 