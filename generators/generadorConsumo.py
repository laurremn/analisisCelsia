import random 
def generarDatos():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["sony","rico","kalley"])
        capacidad=random.randint(100,200)
        ciudad=random.choice(["Medellin","Cali","Pereira","Cartagena","Bucaramanga"])
        responsable=random.choice(["Tomas Agudelo","Laura Restrepo","Lina Areiza","Sara Arango","Laura Perez"])
        dato=[id,referencia,marca,capacidad,ciudad,responsable]
        datos.append(dato)
    return datos 
print(generarDatos())      