datos = {"nombre":"", "edad":"", "direccion":"", "telefono":""}
for i in datos:
    datos[i] = input(f"Ingrese su {i}: ")
print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su numero de telefono es {datos['telefono']}")