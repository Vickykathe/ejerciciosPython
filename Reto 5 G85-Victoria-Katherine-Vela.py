import json
contactos=[("Primera", "Mariana", 34500),
          ( "Segunda","Tatina",15200),
           ("Tercera","Juan",16700),
           ("Primera","Ana",68900),
           ("Segunda","Pedro",74900),
           ("Primera","Manuel",57000),
           ("Tercera","Lorena",87900),
           ("Primera","Javier",95600), 
           ("Segunda","Marta",120300),
            ("Tercera","Mario",890500)]

datos = []
for sucursal, nombre, salab in contactos:
    datos.append({"sucursal":sucursal, "nombre":nombre, "salab":salab})

with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)
    
with open("contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["sucursal"], contacto["nombre"], contacto["salab"])