ListaFrutas = ["Limon", "Fresa", "Manzana", "Mango", "Durazno ","Naranja"]

ListaFrutas.append("Mandarina")    

ListaFrutas[5] = "Sandia"

for fruta in ListaFrutas:
    print(f"fruta: {fruta}")

ListaFrutas.pop(3)      
