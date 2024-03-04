import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Economia"
}
post_response = requests.request(method="POST", url=ruta_post,json=nuevo_estudiante)

# GET obtener todas las carreras
ruta_get = url + "estudiantes/carrera"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# GET busca a los estudiantes por carrera /estudiantes/{carrera}
ruta_filtrar_nombre = url + "estudiantes/Economia"
filtrar_nombre_response = requests.request(method="GET", 
                                url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)

# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Laura",
    "apellido": "Rodriguez",
    "carrera": "Economia"
}
post_response = requests.request(method="POST", url=ruta_post,json=nuevo_estudiante)
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Samuel",
    "apellido": "Ticona",
    "carrera": "Economia"
}
post_response = requests.request(method="POST", url=ruta_post,json=nuevo_estudiante)
print(post_response.text)
